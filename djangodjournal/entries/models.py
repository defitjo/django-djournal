from django.db import models

# Create your models here.
class Entry(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  thumbnail = models.ImageField(blank=True)

  def __str__(self):
    return self.title

  def short_body(self):
    return self.body[:50] + "..."