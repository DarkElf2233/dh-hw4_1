
from django.urls import path
from .views import students_list

app_name = 'phones'

urlpatterns = [
    path('', students_list, name='students'),
]
