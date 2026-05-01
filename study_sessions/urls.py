from django.urls import path
from .views import (
    StartStudySessionView,
    EndStudySessionView,
    StudyHistoryView,
    StudySessionDetailView
)

urlpatterns = [
    path('start/', StartStudySessionView.as_view()),
    path('end/', EndStudySessionView.as_view()),
    path('history/', StudyHistoryView.as_view()),
    path('details/<int:pk>/', StudySessionDetailView.as_view()),
]