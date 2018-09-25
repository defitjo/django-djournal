from django.db import models

# Create your models here.
class Entry(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)