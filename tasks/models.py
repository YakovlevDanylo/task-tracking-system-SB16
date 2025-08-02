from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "TO DO"),
        ("in_progress", "IN PROGRESS"),
        ("complete", "COMPLETE"),
    ]

    PRIORITY_CHOICES = [
        ("low", "LOW PRIORITY"),
        ("middle", "MIDDLE PRIORITY"),
        ("high", "HIGH PRIORITY"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default="middle")
    end_time = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
