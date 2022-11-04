from django.urls import path
from accounts2 import views

urlpatterns = [
    # path('user2/', views.user_list, name = 'user-list'),
    # path('user2/<int:pk>/', views.user_detail, name='user-detail'),
    # path('user3/', views.UserView.as_view(), name='user-filter_data'),
    # path('immunization2/', views.user_immunization_list, name = 'user-immunization-list'),
    # path('immunization2/<int:pk>/', views.user_immunization_detail, name='user-immunization-detail'),


    # GET and POST
    path('users/', views.UserView.as_view(),  name='Users'),
    # GET, PUT, DELETE
    path('users/<int:pk>/', views.UserDetail.as_view(),  name='Users'),
    path('immunizations/', views.ImmunizationLists.as_view(),  name='Users'),
    # can INSERT/CREATE AND SERCAH BY EMAIL OR IMMUNIZATION NAME
    path('user-by-email-or-phone/', views.UsersList.as_view(), name='user-by-email-or-phone'),
    path('immunization-by-name/', views.ImmunizationLists.as_view(), name='Users'),
    
]
