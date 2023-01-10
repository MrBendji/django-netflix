from django.db import models
from django.utils import timezone


CHARS_MAX_LENGTH: int = 150

class Category(models.Model):
    """Category model class."""

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """Tag model class."""

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    """Movie model class."""

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(default=timezone.now)
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')

    def __str__(self):
        return self.name



