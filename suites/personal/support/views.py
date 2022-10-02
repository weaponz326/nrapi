from django.shortcuts import render

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class SupportView(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    def post(self, request, format=None):
        name = request.data['name']
        source = request.data['source']
        email = request.data['email']
        message = request.data['message']

        subject = source + ' - ' + name

        if name and source and email and message:
            try:
                send_mail(subject, message, email, ['weaponz326@gmail.com'])
            except BadHeaderError:
                return HttpResponse(status.HTTP_400_BAD_REQUEST)
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)