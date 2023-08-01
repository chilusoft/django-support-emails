import random

from index.models import SupportEmailResponse, SupportEmail
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse

from index.serializers import SupportEmailResponseSerializer, SupportEmailSerializer

# Create your views here.


class SupportEmailView(generics.ListAPIView):
    queryset = SupportEmail.objects.all()
    serializer_class = SupportEmailSerializer

class SupportEmailResponseView(generics.ListAPIView):
    queryset = SupportEmailResponse.objects.all()
    serializer_class = SupportEmailResponseSerializer


@csrf_exempt
@api_view(['POST'])
def send_support_email(request):
    if request.method == 'POST':
        try:
            # generate support ticket number
            support_ticket_number = 'SUP-' + str(random.randint(100000, 999999))
            while True:
                if SupportEmail.objects.filter(support_ticket=support_ticket_number).exists():
                    support_ticket_number = 'SUP-' + str(random.randint(100000, 999999))
                else:
                    break
            # send email
            send_mail(
                'Support Email',
                'Thank you for contacting us. We will get back to you shortly. Your support ticket number is ' + support_ticket_number + '.',
                None,
                [request.data["sender_email"]],
                fail_silently=False,
            )
            SupportEmail.objects.create(
                subject=request.data['subject'],
                message=request.data['message'],
                sender_email=request.data['sender_email'],
                support_ticket=support_ticket_number,
            )
            return JsonResponse({'status': 'success'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def send_support_email_response(request):
    if request.method == 'POST':
        try:
            support_email = SupportEmail.objects.get(pk=request.data['support_email']['id'])
            support_ticket_number=support_email.support_ticket
            # send email
            send_mail(
                support_ticket_number + ' : ' + support_email.subject,
                request.data['message'] + '\n\n\n\nResponse to \n ' + support_email.message,
                None,
                [support_email.sender_email],
                fail_silently=False,
            )
            SupportEmailResponse.objects.create(
                support_email=support_email,
                message=request.data['message']
            )
            return JsonResponse({'status': 'success'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
