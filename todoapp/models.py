from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    text = models.TextField()
    expires_at = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[::50]