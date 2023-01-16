import glob
import os
import cv2
from .models import *
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
import random

# Sending mail to each participant
def sendMail(subject, message, email_to, certificate_file):
    try:
        email_form = settings.EMAIL_HOST_USER
        certificate = EmailMessage(subject,message,email_form,[email_to])
        certificate.attach_file(certificate_file)
        certificate.send()
    except Exception as e :
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
    x_offset = 652
    y_offset = 1170

    y1, y2 = y_offset, y_offset + signature.shape[0]
    x1, x2 = x_offset, x_offset + signature.shape[1]

    alpha_s = signature[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        template[y1:y2, x1:x2, c] = (
            alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

    random_num = random.randint(1000,9999)
    certificate_id = str(stu_id)+str(department)+str(random_num)+str(year)+str(from_date.replace("-",""))

    cv2.putText(template, name, (676, 632), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
    cv2.putText(template, rank, (1048, 748), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    cv2.putText(template, event, (812, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    cv2.putText(template, certificate_id, (28, 1380), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (10, 10, 10), 1, cv2.LINE_AA)
    # cv2.putText(template, year, (1210, 1034), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    if from_date == to_date:
        cv2.putText(template, from_date, (872, 938), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
    else:
        cv2.putText(template, from_date, (732, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
        cv2.putText(template, to_date, (782, 552), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imwrite(f'./cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+name}.jpg', template)
    
    return certificate_id
        
# Certificate generator
def generateCertificate(request,slug):
    cleanUp()

    event = Event.objects.filter(slug=slug)
    event_list = []
    for eve in event:
        event_list.append(eve.event_name)
        event_list.append(eve.event_department)
        event_list.append(str(eve.from_date))
        event_list.append(str(eve.to_date))
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
        participant_list.append([participant.student_name,participant.student_id,participant.email,participant.certificate_status])

    not_eligible_list = []
    
    for data in participant_list:
        signature = cv2.imread("./cert_gen_sen_app_backend/certificate_data/certificate-generator/Galvin Belson.png", -1)
        template_base_dir = "./cert_gen_sen_app_backend/certificate_data/certificate-generator/"

        if data[3] == "1" or data[3] == "2" or data[3] == "3":
            if data[3] == "1":
                template = cv2.imread(template_base_dir + "certificate_1st.jpg")
                certificate_id = meritCertificateGenerate(data[0],data[1][0:4],data[3]+"st",event_list[0],event_list[1],event_list[2],event_list[3],event_list[4],template,signature)
                sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 1st rank in the event and thank you for participanting in the event.", data[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+data[0]}.jpg')
            elif data[3] == "2":
                template = cv2.imread(template_base_dir + "certificate_2nd.jpg")
                certificate_id = meritCertificateGenerate(data[0],data[1][0:4],data[3]+"nd",event_list[0],event_list[1],event_list[2],event_list[3],event_list[4],template,signature)
                sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 2nd rank in the event and thank you for participanting in the event.", data[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+data[0]}.jpg')
            elif data[3] == "3":
                template = cv2.imread(template_base_dir + "certificate_3rd.jpg")
                certificate_id = meritCertificateGenerate(data[0],data[1][0:4],data[3]+"rd",event_list[0],event_list[1],event_list[2],event_list[3],event_list[4],template,signature)
                sendMail("Certificate of Merit", "CONGRATULATIONS... You have secured 3rd rank in the event and thank you for participanting in the event.", data[2], f'../app/cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(certificate_id)+" "+data[0]}.jpg')
        else:
            if data[3] == "F":
                not_eligible_list.append(data[0])
            else:
                template = cv2.imread(template_base_dir + "certificate_of_completion.jpg")
                x_offset = 578
                y_offset = 1020

                y1, y2 = y_offset, y_offset + signature.shape[0]
                x1, x2 = x_offset, x_offset + signature.shape[1]

                alpha_s = signature[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s

                for c in range(0, 3):
                    template[y1:y2, x1:x2, c] = (
                        alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

                random_num = random.randint(1000,9999)
                certificate_id = str(data[1][0:4])+str(event_list[1])+str(random_num)+str(event_list[4])+str(event_list[2].replace("-",""))

                cv2.putText(template, data[0], (592, 704), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
                cv2.putText(template, event_list[0], (1036, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
                cv2.putText(template, certificate_id, (28, 1380), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (10, 10, 10), 1, cv2.LINE_AA)
                if event_date_check:
                    cv2.putText(template, event_list[2], (730, 886), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                else:
                    cv2.putText(template, event_list[2], (732, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                    # cv2.putText(template, event_list[3], (782, 552), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.imwrite(f'./cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(certificate_id)+" "+data[0]}.jpg', template)
                # sendMail("Certificate of Participation", "Thank you for participanting in the Event/Contest", data[2], f'../app/cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(count)+" "+data[0]}.jpg')
        # print(f'Processing {index + 1} / {len(key)}')
    return JsonResponse("Certificate generated and sended successfully",safe=False)

# Generate certificate by Id
def generateCertificateById(request,slug,pk):
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
        print("1")
        not_eligible = "The Student "+participant_list[0]+" is not eligible for certificate"
        print("2")
        return JsonResponse(not_eligible,safe=False)
    else:
        event_list = []

        event = Event.objects.filter(slug=slug)

        for eve in event:
            event_list.append(eve.event_name)
            event_list.append(eve.event_department)
            event_list.append(str(eve.from_date))
            event_list.append(str(eve.to_date))
            event_list.append(eve.event_year)

        signature = cv2.imread("./cert_gen_sen_app_backend/certificate_data/certificate-generator/Galvin Belson.png", -1)
        template_base_dir = "./cert_gen_sen_app_backend/certificate_data/certificate-generator/"
        template = cv2.imread(template_base_dir + "certificate_of_completion.jpg")

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

        random_num = random.randint(1000,9999)
        certificate_id = str(participant_list[1][0:4])+str(event_list[1])+str(random_num)+str(event_list[4])+str(event_list[2].replace("-",""))

        cv2.putText(template, participant_list[0], (592, 704), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
        cv2.putText(template, event_list[0], (1036, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
        cv2.putText(template, certificate_id, (28, 1380), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (10, 10, 10), 1, cv2.LINE_AA)

        if event_date_check:
            cv2.putText(template, event_list[2], (730, 886), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
        else:
            cv2.putText(template, event_list[2], (732, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
            # cv2.putText(template, event_list[3], (782, 552), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite(f'./cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(certificate_id)+" "+participant_list[0]}.jpg', template)
        # sendMail("Certificate of Participation", "Thank you for participanting in the Event/Contest", participant_list[2], f'../app/cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(count)+" "+participant_list[0]}.jpg')
        return JsonResponse("Certificate generated and sended successfully",safe=False)