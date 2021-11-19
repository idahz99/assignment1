from django.urls import path
from . import views

urlpatterns = [
    path('<int:ic>', views.people, name="person-info"),
    path('page1/', views.people),
    path('Penghulu/', views.penghulu),
    path('peopleInfo_report/', views.peopleinfo_report, name ="peopleinfo"),
    path('Register/', views.register, name="register"),
    path('edit-info', views.edit, name="edit-info"),
]
