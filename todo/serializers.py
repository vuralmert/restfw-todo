from rest_framework import serializers
from django.utils import timezone
from todo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'priority',
            'is_done',
        )



    def validate_deadline(self,value):
        if (timezone.now() > value):
            raise serializers.ValidationError('Deadline must be in the future.')
        return value
