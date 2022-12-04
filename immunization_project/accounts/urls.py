from django.urls import path
from accounts import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<str:email>/', views.user_details),
]
