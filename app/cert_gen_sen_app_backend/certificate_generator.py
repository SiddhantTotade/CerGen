import glob
import os
import cv2
from .models import *
from django.http import JsonResponse
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from django.conf import settings
import random
from collections import OrderedDict
from python_pptx_text_replacer import TextReplacer
import tqdm
import qrcode
from pptx import Presentation
from PIL import Image
import smtplib
import ssl
from twilio.rest import Client
from decouple import config
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_message(student_name, phone):
    account_sid = config("TWILIO_SID")
    auth_token = config("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    client.messages.create(
        body="Thankyou for participating in the Event/Contest. Your certificate will delivered to you via e-mail. Check your email.",
        from_="+15855951968",
        to=f"+91{phone}"
    )
    return JsonResponse("Message sent successfully", safe=False)


def send_mail(subject, body, email_to, certificate_file):
    email_from = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    try:
        message = MIMEMultipart()
        message['From'] = email_from
        message['To'] = email_to
        message['Subject'] = subject
        message['Bcc'] = email_to

        message.attach(MIMEText(body, 'plain'))
        file = certificate_file

        with open(file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition',
                        f"attachment;filename={file.replace('./cert_gen_sen_app_backend/certificate_data/participants-certificates/', '')}")

        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(email_from, password)
            server.sendmail(email_from, email_to, text)

        return "SENT"
    except Exception as e:
        print(e)


# Sending mail to each participant
def sendMail(subject, message, email_to, certificate_file):
    try:
        email_form = settings.EMAIL_HOST_USER
        certificate = EmailMessage(subject, message, email_form, [email_to])
        certificate.attach_file(certificate_file)
        certificate.send()
        return "SENT"
    except Exception as e:
        print(e)


# Certificate directory cleaner
def cleanUp():
    participant_files = "../app/cert_gen_sen_app_backend/certificate_data/participants-certificates"
    participant_filelist = glob.glob(os.path.join(participant_files, "*"))
    for f in participant_filelist:
        os.remove(f)

    merit_files = "../app/cert_gen_sen_app_backend/certificate_data/merit-certificates"
    merit_filelist = glob.glob(os.path.join(merit_files, "*"))
    for f in merit_filelist:
        os.remove(f)


def meritCertificateGenerate(name, stu_id, rank, event, department, from_date, to_date, year, template, signature):
    x_offset = 664
    y_offset = 1090

    y1, y2 = y_offset, y_offset + signature.shape[0]
    x1, x2 = x_offset, x_offset + signature.shape[1]

    alpha_s = signature[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        template[y1:y2, x1:x2, c] = (
            alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

    random_num = random.randint(1000, 9999)
    certificate_id = str(stu_id)+str(department)+str(random_num) + \
        str(year)+str(from_date.replace("-", ""))

    cv2.putText(template, name, (676, 632),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
    cv2.putText(template, rank, (1048, 748),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    cv2.putText(template, event, (812, 838),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    cv2.putText(template, certificate_id, (28, 1380),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (10, 10, 10), 1, cv2.LINE_AA)
    cv2.putText(template, str(year), (1210, 1034),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    if from_date == to_date:
        cv2.putText(template, from_date, (872, 938),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
    else:
        cv2.putText(template, from_date, (866, 938),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
        cv2.putText(template, "to", (1148, 938),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
        cv2.putText(template, to_date, (1238, 938),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
    cv2.imwrite(
        f'./cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+name}.jpg', template)

    return certificate_id


# Placing QR code in PPT
def place_qrcode(pptx_path, qrcode_path, replace_str):
    pptx_file = Presentation(pptx_path)

    for slide in pptx_file.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                if shape.text.find(replace_str) != -1:
                    slide.shapes.add_picture(
                        qrcode_path, shape.left, shape.top)

    pptx_file.save(pptx_path)


# Set size of QR code
def resize_qrcode(qrcode_path):
    img = Image.open(qrcode_path)
    width = 100
    height = 100
    resize = img.resize((width, height), Image.NEAREST)
    resize.save(qrcode_path)


# Generate QR code
def generate_qrcode(stu_name, stu_id, cert_id, eve_name, eve_department, eve_date):
    qr_code = qrcode.QRCode(
        version=5, box_size=2, border=1)
    qr_code.add_data(
        f"Participant Name - {stu_name}\nParticipant Id - {stu_id}\nEvent Name - {eve_name}\nEvent Department - {eve_department}\nEvent Date - {eve_date}\nCertificate Id - {cert_id}")
    type(qr_code)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save(
        f'./cert_gen_sen_app_backend/certificate_data/qr-code/{cert_id} - {stu_name}.png')

    # resize_qrcode(
    #     f'./cert_gen_sen_app_backend/certificate_data/qr-code/{cert_id} - {stu_name}.png')

    return f'./cert_gen_sen_app_backend/certificate_data/qr-code/{cert_id} - {stu_name}.png'


# Generate certificates for all participants type
def generate_participant_certificate(stu_name, cert_id, qrcode_path, completion_certificate_path):
    replacer = TextReplacer(f'../app{completion_certificate_path}',
                            slides="", tables=True, charts=True, textframes=True)

    replacer.replace_text(
        [("{{StudentName}}", stu_name), ("{{UID}}", cert_id)])

    replacer.write_presentation_to_file(
        f'./cert_gen_sen_app_backend/certificate_data/ppt-certificates/{cert_id} - {stu_name}.pptx')

    pptx_path = f'./cert_gen_sen_app_backend/certificate_data/ppt-certificates/{cert_id} - {stu_name}.pptx'

    place_qrcode(pptx_path, qrcode_path, "{{QR}}")

    path = './cert_gen_sen_app_backend/certificate_data/ppt-certificates'
    ext = 'pptx'

    files = [f for f in glob.glob(
        path + "/**/*.{}".format(ext), recursive=True)]

    for f in tqdm.tqdm(files):
        command = "unoconv -f pdf \"{}\"".format(f)
        move_file = "mv ./cert_gen_sen_app_backend/certificate_data/ppt-certificates/*.pdf ./cert_gen_sen_app_backend/certificate_data/participants-certificates/"
        os.system(command)
        os.system(move_file)

    return f'./cert_gen_sen_app_backend/certificate_data/participants-certificates/{cert_id} - {stu_name}.pdf'


# Generate certificates for merit participants
def generate_merit_certificate(stu_name, cert_id, rank, qrcode_path, merit_certificate_path):
    replacer = TextReplacer(f'../app{merit_certificate_path}',
                            slides="", tables=True, charts=True, textframes=True)

    if (rank == "1"):
        replacer.replace_text(
            [("{{StudentName}}", stu_name), ("{{UID}}", cert_id), ("{{POS}}", f"{rank} st")])
    elif (rank == "2"):
        replacer.replace_text(
            [("{{StudentName}}", stu_name), ("{{UID}}", cert_id), ("{{POS}}", f"{rank} nd")])
    elif (rank == "3"):
        replacer.replace_text(
            [("{{StudentName}}", stu_name), ("{{UID}}", cert_id), ("{{POS}}", f"{rank} rd")])

    replacer.write_presentation_to_file(
        f'./cert_gen_sen_app_backend/certificate_data/ppt-certificates/{cert_id} - {stu_name}.pptx')

    pptx_path = f'./cert_gen_sen_app_backend/certificate_data/ppt-certificates/{cert_id} - {stu_name}.pptx'

    place_qrcode(pptx_path, qrcode_path, "{{QR}}")

    path = './cert_gen_sen_app_backend/certificate_data/ppt-certificates'
    ext = 'pptx'

    files = [f for f in glob.glob(
        path + "/**/*.{}".format(ext), recursive=True)]

    for f in tqdm.tqdm(files):
        command = "unoconv -f pdf \"{}\"".format(f)
        move_file = "mv ./cert_gen_sen_app_backend/certificate_data/ppt-certificates/*.pdf ./cert_gen_sen_app_backend/certificate_data/participants-certificates/"
        os.system(command)
        os.system(move_file)

    return f'./cert_gen_sen_app_backend/certificate_data/merit-certificates/{cert_id} - {stu_name}.pdf'


# Generate certificates for all
class GenerateCertificate(APIView):
    def post(self, request, slug):
        obj_event = Event.objects.get(slug=slug)
        event = Event.objects.filter(slug=slug)
        participants = Participant.objects.filter(event=obj_event)

        completion_certificate_path = request.data['completion']
        merit_certificate_path = request.data['merit']

        stu_data = []
        eve_data = OrderedDict()

        for stu in participants:
            if stu.certificate_sent_status == False:
                if stu.certificate_status == 'T' or stu.certificate_status == '1' or stu.certificate_status == '2' or stu.certificate_status == '3':
                    stu_data.append(dict(id=stu.id, student_name=stu.student_name, student_id=stu.student_id, email=stu.email,
                                         certificate_status=stu.certificate_status, certificate_id=stu.certificate_id))

        for eve in event:
            eve_data['event_name'] = eve.event_name
            eve_data['event_department'] = eve.event_department
            eve_data['from_date'] = eve.from_date.strftime('%d-%m-%Y')

        for stu in stu_data:
            if stu['certificate_status'] == "1" or stu['certificate_status'] == "2" or stu['certificate_status'] == "3":
                qrcode_path = generate_qrcode(
                    stu["student_name"], stu["student_id"], stu["certificate_id"], eve_data["event_name"], eve_data["event_department"], eve_data["from_date"])
                certificate_path = generate_merit_certificate(
                    stu['student_name'], stu['certificate_id'], stu['certificate_status'], qrcode_path, merit_certificate_path)
                # send_certificate = send_mail("Certificate of Participation",
                #                              "Thank you for participanting in the Event/Contest", stu["email"], certificate_path)

                # if send_certificate == "SENT":
                #     Participant.objects.filter(
                #         id=stu['id']).update(certificate_sent_status=True)
            else:
                qrcode_path = generate_qrcode(
                    stu["student_name"], stu["student_id"], stu["certificate_id"], eve_data["event_name"], eve_data["event_department"], eve_data["from_date"])
                certificate_path = generate_participant_certificate(
                    stu["student_name"], stu["certificate_id"], qrcode_path, completion_certificate_path)
                send_certificate = send_mail("Certificate of Participation",
                                             "Thank you for participanting in the Event/Contest", stu["email"], certificate_path)

                if send_certificate == "SENT":
                    Participant.objects.filter(
                        id=stu['id']).update(certificate_sent_status=True)

        return JsonResponse("Certificate generated and sended successfully", safe=False)
        # return JsonResponse("Some problem occured while sending", safe=False)


# Generate certificates for specific participant
def generate_certificate_by_id(request, slug, pk):
    participant = Participant.objects.filter(id=pk)
    event = Event.objects.filter(slug=slug)

    stu_data = OrderedDict()
    eve_data = OrderedDict()

    for stu in participant:
        stu_data['student_name'] = stu.student_name
        stu_data['student_id'] = stu.student_id
        stu_data['email'] = stu.email
        stu_data['certificate_status'] = stu.certificate_status
        stu_data['certificate_id'] = stu.certificate_id

    for eve in event:
        eve_data['event_name'] = eve.event_name
        eve_data['event_department'] = eve.event_department
        eve_data['from_date'] = eve.from_date.strftime('%d-%m-%Y')

    if stu_data["certificate_status"] == 'F' or stu_data["certificate_status"] == None:
        return JsonResponse("This participant is not eligible for certificate", safe=False)
    elif stu_data["certificate_status"] == '1' or stu_data["certificate_status"] == '2' or stu_data["certificate_status"] == '3':
        generate_merit_certificate(
            stu_data["name"], stu_data["certificate_id"], stu_data["certificate_status"])
    else:
        qrcode_path = generate_qrcode(
            stu_data["student_name"], stu_data["student_id"], stu_data["certificate_id"], eve_data["event_name"], eve_data["event_department"], eve_data["from_date"])
        certificate_path = generate_participant_certificate(
            stu_data["student_name"], stu_data["certificate_id"], qrcode_path)
        send_certificate = send_mail("Certificate of Participation",
                                     "Thank you for participanting in the Event/Contest", stu_data["email"], certificate_path)

        if send_certificate == "SENT":
            Participant.objects.filter(
                id=pk).update(certificate_sent_status=True)
            return JsonResponse("Certificate generated and sended successfully", safe=False)

    return JsonResponse("Some problem occured while sending", safe=False)
