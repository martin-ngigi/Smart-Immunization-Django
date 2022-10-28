from django.shortcuts import render

# Create your views here.

from dataclasses import dataclass
from django.http import JsonResponse
from django.urls import is_valid_path
from .models import Immunizations
from .serializers import ImmunizationsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#either fetch or create
@api_view(['GET', 'POST'])
def immn_list(request, format=None):
    # fetch data
    if request.method == 'GET':
        # get python data
        # serialize it
        # return json data

        immn = Immunizations.objects.all()
        serializer = ImmunizationsSerializer(immn, many=True)
        return Response(serializer.data)

    #create data
    if request.method == 'POST':
        # get json data
        # deserialize it
        # return python data

        serializer = ImmunizationsSerializer(data = request.data)
        # validate
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

# Either fetch, update or delete
@api_view(['GET', 'PUT', 'DELETE'])
def immn_details(request, id, format=None): #id is from urls.py
    try:
        immn = Immunizations.objects.get(pk=id)
    except Immunizations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Fetch
    if request.method == 'GET':
        serializer = ImmunizationsSerializer(immn)
        return Response(serializer.data)
    
    # Update
    elif request.method == 'PUT':
        serializer = Immunizations(immn, data = request.data)
        # if serialize is valid, then save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # else show error message
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        immn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)