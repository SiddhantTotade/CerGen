from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.conf import settings
from .models import *
import os
import random
import string
import base64


class Ppt2Image(APIView):
    def clear_preview(self):
        clear_command = 'rm -rf ./cert_gen_sen_app_backend/certificate_data/preview-template-ppts/*'
        os.system(clear_command)

    def post(self, request):
        self.clear_preview()
        letters_and_digits = string.ascii_letters + string.digits
        file_name_str = "".join(random.choice(
            letters_and_digits)for i in range(15))

        pptx_file = request.FILES['pptx_file']
        file_name = file_name_str + pptx_file.name

        img_file_name = os.path.splitext(file_name)[0]

        file_path = os.path.join(
            settings.BASE_DIR, './cert_gen_sen_app_backend/certificate_data/preview-template-ppts/', file_name)

        with open(file_path, 'wb+') as destination:
            for chunk in pptx_file.chunks():
                destination.write(chunk)

        preview_image_command = f'unoconv -f jpg ./cert_gen_sen_app_backend/certificate_data/preview-template-ppts/{file_name}'
        os.system(preview_image_command)

        with open(f'./cert_gen_sen_app_backend/certificate_data/preview-template-ppts/{img_file_name}.jpg', 'rb') as img:
            str = base64.b64encode(img.read())

        # response = HttpResponse(
        #     str, content_type='image/jpg')
        # response['Content-Disposition'] = f'attachment; filename={file_name}'

        # self.clear_preview()

        return Response(str)
