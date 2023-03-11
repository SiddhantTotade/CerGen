import aspose.slides as slides
# import aspose.pydrwaing as drawing
from django.http import JsonResponse


def ppttohtml(self, request):
    print(request.data)

    return JsonResponse("OK", safe=False)
