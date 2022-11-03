from django.urls import path
from accounts2 import views

urlpatterns = [
    path('user2/', views.user_list, name = 'user-list'),
    path('user2/<int:pk>/', views.user_detail, name='user-detail'),
    path('immunization2/', views.user_immunization_list, name = 'user-immunization-list'),
    path('immunization2/<int:pk>/', views.user_immunization_detail, name='user-immunization-detail'),
    
]
