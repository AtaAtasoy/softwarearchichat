from django.db import models
from django.contrib.auth.models import User

class ChatModel(models.Model):
    sender = models.CharField(max_length=50, blank=False, default=None)
    message = models.TextField(null=True, blank=True)
    room_name = models.CharField(null=True, blank=True, max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message