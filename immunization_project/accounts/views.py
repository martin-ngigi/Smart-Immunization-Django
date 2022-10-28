from django.shortcuts import render

# Create your views here.

from dataclasses import dataclass
from django.http import JsonResponse
from django.urls import is_valid_path
from .models import MyUser
from .serializers import MyUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#either fetch or create
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    # fetch data
    if request.method == 'GET':
        # get python data
        # serialize it
        # return json data

        myUsers = MyUser.objects.all()
        serializer = MyUserSerializer(myUsers, many=True)
        return Response(serializer.data)

    #create data
    if request.method == 'POST':
        # get json data
        # deserialize it
        # return python data

        serializer = MyUserSerializer(data = request.data)
        # validate
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

# Either fetch, update or delete
@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, id, format=None):
    try:
        myUser = MyUser.objects.get(pk=id)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Fetch
    if request.method == 'GET':
        serializer = MyUserSerializer(myUser)
        return Response(serializer.data)
    
    # Update
    elif request.method == 'PUT':
        serializer = MyUserSerializer(myUser, data = request.data)
        # if serialize is valid, then save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # else show error message
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        myUser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)