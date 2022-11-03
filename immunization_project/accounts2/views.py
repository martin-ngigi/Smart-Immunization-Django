from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from accounts2.models import User, UserImmunization
from accounts2.serializers import UserSerializer, UserImmunizationSerializer

@csrf_exempt
def user_list(request):
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
def user_detail(request, pk):
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
def user_immunization_list(request):
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
def user_immunization_detail(request, pk):
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
