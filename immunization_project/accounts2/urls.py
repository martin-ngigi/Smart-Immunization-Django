from django.urls import path
from accounts2 import views

urlpatterns = [
    path('user2/', views.employee_list, name = 'employee-list'),
    path('user2/<int:pk>/', views.employee_detail, name='employee-detail'),
    path('immunization2/', views.employeetask_list, name = 'employeetask-list'),
    path('immunization2/<int:pk>/', views.employeetask_detail, name='employeetask-detail'),
    
]
