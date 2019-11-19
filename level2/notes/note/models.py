from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
