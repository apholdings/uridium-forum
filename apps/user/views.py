from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.db.models.query_utils import Q
from django.conf import settings
domain = settings.DOMAIN
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseBadRequest

from .models import UserAccount

class CreateUserProfileView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):

        data = self.request.data

        account = data["account"]