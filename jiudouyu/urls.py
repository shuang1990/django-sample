from django.urls import path

from . import views

app_name="jdy"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.user_list, name='list'),
    path('register/', views.register, name='register'),
    path('identify/', views.identify, name='identify'),
    path('info/<int:user_id>/', views.user_info, name='info'),
    path('change/', views.edit_name, name='change'),
    path('delete/<int:user_id>/', views.delete_user, name='delete'),
    path('request-test/', views.request_test, name='request-test'),

]