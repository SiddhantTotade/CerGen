import glob
import os
import cv2
from .models import *
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
import random
from collections import OrderedDict
from python_pptx_text_replacer import TextReplacer
import tqdm
import qrcode
from pptx.util import Inches
from pptx import shapes, Presentation
from PIL import Image

# Sending mail to each participant


def sendMail(subject, message, email_to, certificate_file):
    try:
        email_form = settings.EMAIL_HOST_USER
        certificate = EmailMessage(subject, message, email_form, [email_to])
        certificate.attach_file(certificate_file)
        certificate.send()
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

# Certificate generator


def generateCertificate(request, slug):
    cleanUp()

    event = Event.objects.filter(slug=slug)
    event_list = []
    for eve in event:
        event_list.append(eve.event_name)
        event_list.append(eve.event_department)
        event_list.append(str(eve.from_date.strftime('%d-%m-%Y')))
        event_list.append(str(eve.to_date.strftime('%d-%m-%Y')))
        event_list.append(eve.event_year)

    event_date_check = False
    if event_list[2] == event_list[3]:
        event_date_check = True

    new_event_id = 0
    for event_id in event:
        new_event_id = event_id

    participants = Participant.objects.filter(event=new_event_id)

    participant_list = []
    for participant in participants:
        participant_list.append([participant.student_name, participant.student_id,
                                participant.email, participant.certificate_status])

    not_eligible_list = []

    for data in participant_list:
        signature = cv2.imread(
            "./cert_gen_sen_app_backend/certificate_data/certificate-generator/Galvin Belson.png", -1)
        template_base_dir = "./cert_gen_sen_app_backend/certificate_data/certificate-generator/"

        if data[3] == "1" or data[3] == "2" or data[3] == "3":
            if data[3] == "1":
                template = cv2.imread(
                    template_base_dir + "certificate_1st.jpg")
                certificate_id = meritCertificateGenerate(
                    data[0], data[1][0:4], data[3]+"st", event_list[0], event_list[1], event_list[2], event_list[3], event_list[4], template, signature)
                sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 1st rank in the event and thank you for participanting in the event.",
                         data[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+data[0]}.jpg')
            elif data[3] == "2":
                template = cv2.imread(
                    template_base_dir + "certificate_2nd.jpg")
                certificate_id = meritCertificateGenerate(
                    data[0], data[1][0:4], data[3]+"nd", event_list[0], event_list[1], event_list[2], event_list[3], event_list[4], template, signature)
                sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 2nd rank in the event and thank you for participanting in the event.",
                         data[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+data[0]}.jpg')
            elif data[3] == "3":
                template = cv2.imread(
                    template_base_dir + "certificate_3rd.jpg")
                certificate_id = meritCertificateGenerate(
                    data[0], data[1][0:4], data[3]+"rd", event_list[0], event_list[1], event_list[2], event_list[3], event_list[4], template, signature)
                sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 3rd rank in the event and thank you for participanting in the event.",
                         data[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+data[0]}.jpg')
        else:
            if data[3] == "F":
                not_eligible_list.append(data[0])
            else:
                template = cv2.imread(
                    template_base_dir + "certificate_of_completion.jpg")
                x_offset = 578
                y_offset = 1020

                y1, y2 = y_offset, y_offset + signature.shape[0]
                x1, x2 = x_offset, x_offset + signature.shape[1]

                alpha_s = signature[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s

                for c in range(0, 3):
                    template[y1:y2, x1:x2, c] = (
                        alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

                random_num = random.randint(1000, 9999)
                certificate_id = str(data[1][0:4])+str(event_list[1])+str(
                    random_num)+str(event_list[4])+str(event_list[2].replace("-", ""))

                cv2.putText(
                    template, data[0], (592, 704), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
                cv2.putText(template, event_list[0], (
                    1036, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
                cv2.putText(template, certificate_id, (28, 1380),
                            cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (10, 10, 10), 1, cv2.LINE_AA)
                if event_date_check:
                    cv2.putText(template, event_list[2], (
                        730, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                else:
                    cv2.putText(template, event_list[2], (
                        706, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                    cv2.putText(template, "to", (966, 914),
                                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                    cv2.putText(template, event_list[3], (
                        1034, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                cv2.imwrite(
                    f'./cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(certificate_id)+" "+data[0]}.jpg', template)
                sendMail("Certificate of Participation", "Thank you for participanting in the Event/Contest",
                         data[2], f'../app/cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(certificate_id)+" "+data[0]}.jpg')
    return JsonResponse("Certificate generated and sended successfully", safe=False)

# Generate certificate by Id


def generateCertificateById(request, slug, pk):
    cleanUp()

    participant = Participant.objects.filter(id=pk)

    participant_list = []
    for stu in participant:
        participant_list.append(stu.student_name)
        participant_list.append(stu.student_id)
        participant_list.append(stu.email)
        participant_list.append(stu.certificate_status)

    not_eligible = ""

    if participant_list[3] == "F":
        not_eligible = "The Student " + \
            participant_list[0]+" is not eligible for certificate"
        return JsonResponse(not_eligible, safe=False)
    else:
        event_list = []

        event = Event.objects.filter(slug=slug)

        for eve in event:
            event_list.append(eve.event_name)
            event_list.append(eve.event_department)
            event_list.append(str(eve.from_date))
            event_list.append(str(eve.to_date))
            event_list.append(eve.event_year)

        signature = cv2.imread(
            "./cert_gen_sen_app_backend/certificate_data/certificate-generator/Galvin Belson.png", -1)
        template_base_dir = "./cert_gen_sen_app_backend/certificate_data/certificate-generator/"

        if participant_list[3] == "1":
            template = cv2.imread(template_base_dir + "certificate_1st.jpg")
            certificate_id = meritCertificateGenerate(participant_list[0], participant_list[1][0:4], participant_list[3] +
                                                      "st", event_list[0], event_list[1], event_list[2], event_list[3], event_list[4], template, signature)
            sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 1st rank in the event and thank you for participanting in the event.",
                     participant_list[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+participant_list[0]}.jpg')
        elif participant_list[3] == "2":
            template = cv2.imread(template_base_dir + "certificate_2nd.jpg")
            certificate_id = meritCertificateGenerate(participant_list[0], participant_list[1][0:4], participant_list[3] +
                                                      "nd", event_list[0], event_list[1], event_list[2], event_list[3], event_list[4], template, signature)
            sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 2nd rank in the event and thank you for participanting in the event.",
                     participant_list[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+participant_list[0]}.jpg')
        elif participant_list[3] == "3":
            template = cv2.imread(template_base_dir + "certificate_3rd.jpg")
            certificate_id = meritCertificateGenerate(participant_list[0], participant_list[1][0:4], participant_list[3] +
                                                      "3rd", event_list[0], event_list[1], event_list[2], event_list[3], event_list[4], template, signature)
            sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 3rd rank in the event and thank you for participanting in the event.",
                     participant_list[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+participant_list[0]}.jpg')
        else:
            template = cv2.imread(template_base_dir +
                                  "certificate_of_completion.jpg")

            event_date_check = False
            if event_list[2] == event_list[3]:
                event_date_check = True

            x_offset = 578
            y_offset = 1020
            y1, y2 = y_offset, y_offset + signature.shape[0]
            x1, x2 = x_offset, x_offset + signature.shape[1]
            alpha_s = signature[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s

            for c in range(0, 3):
                template[y1:y2, x1:x2, c] = (
                    alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

            random_num = random.randint(1000, 9999)
            certificate_id = str(participant_list[1][0:4])+str(event_list[1])+str(
                random_num)+str(event_list[4])+str(event_list[2].replace("-", ""))

            cv2.putText(template, participant_list[0], (
                592, 704), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
            cv2.putText(template, event_list[0], (
                1036, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
            cv2.putText(template, certificate_id, (28, 1380),
                        cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (10, 10, 10), 1, cv2.LINE_AA)

            if event_date_check:
                cv2.putText(template, event_list[2], (
                    730, 886), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
            else:
                cv2.putText(template, event_list[2], (
                    706, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                cv2.putText(template, "to", (966, 914),
                            cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                cv2.putText(template, event_list[3], (
                    1034, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
            cv2.imwrite(
                f'./cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(certificate_id)+" "+participant_list[0]}.jpg', template)
            sendMail("Certificate of Participation", "Thank you for participanting in the Event/Contest",
                     participant_list[2], f'../app/cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(certificate_id)+" "+participant_list[0]}.jpg')
    return JsonResponse("Certificate generated and sended successfully", safe=False)


def place_qrcode(pptx_path, qrcode_path, replace_str):
    pptx_file = Presentation(pptx_path)

    for slide in pptx_file.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                if shape.text.find(replace_str) != -1:
                    slide.shapes.add_picture(
                        qrcode_path, shape.left, shape.top)

    pptx_file.save(pptx_path)


def resize_qrcode(qrcode_path):
    img = Image.open(qrcode_path)
    width = 100
    height = 100
    resize = img.resize((width, height), Image.NEAREST)
    resize.save(qrcode_path)


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


def generate_participant_certificate(stu_name, cert_id, qrcode_path):
    replacer = TextReplacer('./cert_gen_sen_app_backend/certificate_data/certificate-template/certificate_of_completion.pptx',
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


def generate_merit_certificate(stu_name, cert_id, cert_status):
    pass


def generate_certificate_by_id(request, slug, pk):
    participant = Participant.objects.filter(id=pk)
    event = Event.objects.filter(slug=slug)

    stu_data = OrderedDict()
    eve_data = OrderedDict()

    for stu in participant:
        stu_data['name'] = stu.student_name
        stu_data['student_id'] = stu.student_id
        stu_data['email'] = stu.email
        stu_data['certificate_status'] = stu.certificate_status
        stu_data['certificate_id'] = stu.certificate_id

    for eve in event:
        eve_data['event_name'] = eve.event_name
        eve_data['event_department'] = eve.event_department
        eve_data['from_date'] = eve.from_date.strftime('%d-%m-%Y')

    if stu_data["certificate_status"] == 'F':
        return JsonResponse("This participant is not eligible for certificate", safe=False)
    elif stu_data["certificate_status"] == '1' or stu_data["certificate_status"] == '2' or stu_data["certificate_status"] == '3':
        generate_merit_certificate(
            stu_data["name"], stu_data["certificate_id"], stu_data["certificate_status"])
    else:
        qrcode_path = generate_qrcode(
            stu_data["name"], stu_data["student_id"], stu_data["certificate_id"], eve_data["event_name"], eve_data["event_department"], eve_data["from_date"])
        certificate_path = generate_participant_certificate(
            stu_data["name"], stu_data["certificate_id"], qrcode_path)
        sendMail("Certificate of Participation",
                 "Thank you for participanting in the Event/Contest", stu_data["email"], certificate_path)

    return JsonResponse("Certificate Generated", safe=False)
