from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('register/<int:course_id>/', views.register_student, name='register_student'),
    path('create/', views.create_course, name='create_course'),

]
