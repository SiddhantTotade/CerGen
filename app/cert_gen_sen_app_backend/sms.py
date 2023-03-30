from rest_framework.views import APIView
from django.http import JsonResponse
from twilio.rest import Client
from decouple import config


class SendMessage(APIView):
    def get(self, request):
        account_sid = config("TWILIO_SID")
        auth_token = config("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)
        client.messages.create(
            body="Thankyou for participating in the Event/Contest. Your certificate will delivered to you via e-mail. Check your email.",
            from_="+15855951968",
            to="+917000417412"
        )
        return JsonResponse("Message sent successfully", safe=False)
