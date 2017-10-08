# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers , generics
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def view_users(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

