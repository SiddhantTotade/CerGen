import aspose.slides as slides
from django.http import JsonResponse


def ppt_2_html(self, request):
    print(request.data)

    return JsonResponse("OK", safe=False)
