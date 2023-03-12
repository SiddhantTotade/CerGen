# import aspose.pydrwaing as drawing
from django.http import JsonResponse
from .models import *


def ppttohtml(request):
    event = Event.objects.all()
    print(request.FILES.get('pptx_file'))

    return JsonResponse("OK", safe=False)
