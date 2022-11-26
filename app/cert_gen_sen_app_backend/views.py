from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *
import pandas as pd
import glob
import os
import cv2

# Create your views here.

class AllEvents(APIView):
    def get(self, request):
        all_events = Event.objects.all()

        if all_events:
            event_serializer_data = EventSerializer(all_events,many=True)
            return JsonResponse(event_serializer_data.data,safe=False)
        return JsonResponse("No Data",safe=False)
    
class FilteredEvent(APIView):
    def get(self, request, slug):
        event = Event.objects.filter(slug=slug)

        if event:
            event_serializer = EventSerializer(event,many=True)
            return JsonResponse(event_serializer.data,safe=False)
        return JsonResponse("No Data",safe=False)

def cleanUp():
    files = glob.glob('generated-certificates/*')
    for f in files:
        os.remove(f)

def generateCertificate(self,request):
    cleanUp()

    from_date = []
    to_date = []
    df = pd.read_excel('Contact Information.xlsx', index_col=None)
    key = df['Full Name'].tolist()
    from_dates = df['Event From Date'].tolist()
    to_dates = df['Event To Date'].tolist()
    for date in from_dates:
        from_date.append(str(date.date()))

    for index, names in enumerate(key):
        template = cv2.imread("certificate-generator/certificate-template.jpg")
        signature = cv2.imread("certificate-generator/Galvin Belson.png", -1)

        x_offset = y_offset = 500

        y1, y2 = y_offset, y_offset + signature.shape[0]
        x1, x2 = x_offset, x_offset + signature.shape[1]

        alpha_s = signature[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            template[y1:y2, x1:x2, c] = (
                alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

        cv2.putText(template, names, (500, 405),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(template, from_date[index], (782, 552),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificates/{names}.jpg', template)
        print(f'Processing {index + 1} / {len(key)}')