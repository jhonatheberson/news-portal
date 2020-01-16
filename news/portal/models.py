from django.db import models

class News(models.Model):
  title = models.CharField(max_length=40)
  portal = models.CharField(max_length=30)

  def __str__(self):
      return self.title
  

# Create your models here.
