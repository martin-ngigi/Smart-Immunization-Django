from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from accounts2.models import User, UserImmunization
from accounts2.serializers import UserSerializer, UserImmunizationSerializer

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

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    #create data
    if request.method == 'POST':
        # get json data
        # deserialize it
        # return python data

        serializer = UserSerializer(data = request.data)
        # validate
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)



# Either fetch, update or delete
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None): #id is from urls.py
    try:
        user = User.objects.get(pk=pk)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Fetch
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    # Update
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        # if serialize is valid, then save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # else show error message
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
@csrf_exempt
def user_list1(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
        
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data,status=201)
        return JsonResponse(user_serializer.errors,status=400)
        
@csrf_exempt
def user_detail1(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
        
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def user_immunization_list1(request):
    if request.method == 'GET':
        user_immunization = UserImmunization.objects.all()
        user_immunization_serializer = UserImmunizationSerializer(user_immunization, many=True)
        return JsonResponse(user_immunization_serializer.data, safe=False)
    elif request.method == 'POST':
        user_immunization_data = JSONParser().parse(request)
        user_immunization_serializer = UserImmunizationSerializer(data=user_immunization_data)
        if user_immunization_serializer.is_valid():
            user_immunization_serializer.save()
            return JsonResponse(user_immunization_serializer.data,status=201)
        return JsonResponse(user_immunization_serializer.errors,status=400)


@csrf_exempt
def user_immunization_detail1(request, pk):
    try:
        user_immunization = UserImmunization.objects.get(pk=pk)
    except UserImmunization.DoesNotExist:
        return HTTPResponse(status=404)
        
    if request.method == 'GET':
        user_immunization_serializer = UserImmunizationSerializer(user_immunization)
        return JsonResponse(user_immunization_serializer.data)
        
    elif request.method == 'DELETE':
        user_immunization.delete()
        return HttpResponse(status=204)
'''
#either fetch or create
@api_view(['GET', 'POST'])
def user_immunization_list(request, format=None):
    # fetch data
    if request.method == 'GET':
        # get python data
        # serialize it
        # return json data

        immn = UserImmunization.objects.all()
        serializer = UserImmunizationSerializer(immn, many=True)
        return Response(serializer.data)

    #create data
    if request.method == 'POST':
        # get json data
        # deserialize it
        # return python data

        serializer = UserImmunizationSerializer(data = request.data)
        # validate
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)



# Either fetch, update or delete
@api_view(['GET', 'PUT', 'DELETE'])
def user_immunization_detail(request, pk, format=None): #id is from urls.py
    try:
        userimmn = UserImmunization.objects.get(pk=pk)
    except UserImmunization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Fetch
    if request.method == 'GET':
        serializer = UserImmunizationSerializer(userimmn)
        return Response(serializer.data)
    
    # Update
    elif request.method == 'PUT':
        serializer = UserImmunizationSerializer(userimmn, data = request.data)
        # if serialize is valid, then save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # else show error message
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        userimmn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


