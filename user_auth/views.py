# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers , generics
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

def view_users(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

