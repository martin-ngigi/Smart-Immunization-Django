from django.urls import path
from immunization import views

urlpatterns =[
    path('', views.immn_list),
    path('<int:id>/', views.immn_details)
]