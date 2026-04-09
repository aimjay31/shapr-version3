from rest_framework import serializers
from .models import StudySession

class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = [
            'id',
            'user',
            'start_time',
            'end_time',
            'duration',
            'subject',
            'productivity_rating',
            'created_at'
        ]
        read_only_fields = ['user', 'created_at']