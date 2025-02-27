from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    status_choices = [ 
        ("terminer", "Terminer"), 
        ("encours", "En cours"), 
    ]
    status = models.CharField(max_length=20, choices=status_choices, default="encours") # Added status field

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        