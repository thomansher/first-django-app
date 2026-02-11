from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
