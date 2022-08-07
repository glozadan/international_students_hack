from rest_framework import serializers
from students.models import Student


class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LoginStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'username',
            'password'
        )
