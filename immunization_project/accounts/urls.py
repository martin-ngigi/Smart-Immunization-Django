from django.urls import path
from accounts import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:id>/', views.user_details),
]
