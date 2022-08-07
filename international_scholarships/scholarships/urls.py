from django.urls import path
from scholarships import views

urlpatterns = [
    path('', views.ScholarshipView.as_view()),
    path('<int:id>', views.ScholarshipSingleView.as_view())
]
