from rest_framework import serializers
from inductionStudents.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'year', 'first_name', 'surname', 'knows_python', 'likes_godot', 'rate_interest']