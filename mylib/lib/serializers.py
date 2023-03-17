from rest_framework import serializers
from .models import Add_Book, student, Issue


class Add_book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Book
        fields = "__all__"

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model= student
        fields='__all__'

class Issue_serializer(serializers.ModelSerializer):
    class Meta:
        model= Issue
        fields='__all__'

