from django.db import models
from datetime import datetime


class Todo(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    PRIORITY_CHOICES = ((LOW, 'Low'),(MEDIUM, 'Medium'), (HIGH, 'High'))

    title = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=1, choices=PRIORITY_CHOICES)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
