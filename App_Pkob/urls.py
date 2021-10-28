from django.urls import path
from . import views

urlpatterns = [
    path('peopleInfo/', views.people),
    path('page1/', views.people),
    path('Penghulu/', views.penghulu),
    path('peopleInfo_report', views.peopleinfo_report),
]
