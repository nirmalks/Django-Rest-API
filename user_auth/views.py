# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UsersList(APIView):

    def get(self, request , format= None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


