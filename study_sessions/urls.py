from django.urls import path
from .views import (
    StartStudySessionView,
    EndStudySessionView,
    StudyHistoryView,
    StudySessionDetailView
)

urlpatterns = [
    path('study/start/', StartStudySessionView.as_view()),
    path('study/end/', EndStudySessionView.as_view()),
    path('study/history/', StudyHistoryView.as_view()),
    path('study/<int:pk>/', StudySessionDetailView.as_view()),
]