from django.urls import path
from .views import StudentListView, StudentUpdateView


urlpatterns = [
    path('student/', StudentListView.as_view()),
    path('student/<int:id>/', StudentUpdateView.as_view()),
]