from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  thumbnail = models.ImageField(blank=True)

  def __str__(self):
    return self.title

  def short_body(self):
    return self.body[:100] + "..."