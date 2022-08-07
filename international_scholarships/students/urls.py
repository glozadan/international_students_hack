from django.urls import path
from .views import LoginStudentView, RegisterStudentView, LoginStudentSerializer

urlpatterns = [
    path('register/', RegisterStudentView.as_view()),
    #path('login/', LoginStudentView.as_view()),
]