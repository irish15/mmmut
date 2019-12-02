from django.conf import settings
from django.db import models
from django.utils import timezone


# class Photo(models.Model):
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)    
    image = models.ImageField(upload_to='photos/', default='SOME STRING')
    gray = models.ImageField(default='Not Set')
    # output = models.ImageField()
    # title = models.CharField(max_length=150)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

