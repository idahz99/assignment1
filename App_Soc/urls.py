from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student),
    path('lecturer/', views.lecturer),
]