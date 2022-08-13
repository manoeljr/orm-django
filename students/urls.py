from django.urls import path

from students import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student_data'),
]