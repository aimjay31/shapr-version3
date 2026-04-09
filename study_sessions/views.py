from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import StudySession
from .serializers import StudySessionSerializer

# Create your views here.

class StartStudySessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session = StudySession.objects.create(
            user=request.user,
            start_time=timezone.now(),
            subject=request.data.get("subject"),
            productivity_rating=request.data.get("productivity_rating", 0)
        )
        serializer = StudySessionSerializer(session)
        return Response(serializer.data)

class EndStudySessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            session = StudySession.objects.filter(
                user=request.user,
                end_time__isnull=True
            ).latest('start_time')
        except StudySession.DoesNotExist:
            return Response({"error": "No active session"}, status=400)

        session.end_time = timezone.now()

        duration = (session.end_time - session.start_time).total_seconds() / 60
        session.duration = int(duration)

        session.save()

        serializer = StudySessionSerializer(session)
        return Response(serializer.data)

class StudyHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sessions = StudySession.objects.filter(user=request.user).order_by('-start_time')
        serializer = StudySessionSerializer(sessions, many=True)
        return Response(serializer.data)

class StudySessionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            session = StudySession.objects.get(id=pk, user=request.user)
        except StudySession.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = StudySessionSerializer(session)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            session = StudySession.objects.get(id=pk, user=request.user)
        except StudySession.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        session.delete()
        return Response({"message": "Deleted successfully"})