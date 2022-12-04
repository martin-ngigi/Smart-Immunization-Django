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

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.views import APIView

from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework import generics

# # MY SIMPLE APIVIEW
class UserView(APIView):
    # List all snippets, or create a new snippet.
    def get(self, request):
        users = User.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SERACH BY EMAIL OR PHONE.(can GET, POST,SEARCH)
class UsersList(generics.ListCreateAPIView):
    # eg: http://127.0.0.1:8000/user-by-email-or-phone?search=martinwainaina001@gmail.com
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email', 'password']

# SERACH BY immunizationName
class ImmunizationLists(generics.ListCreateAPIView):
    queryset = UserImmunization.objects.all()
    serializer_class = UserImmunizationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['immunizationName']

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
    except User.DoesNotExist:
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


