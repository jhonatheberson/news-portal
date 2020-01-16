from django.db import models


class Portal(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    portal = models.ForeignKey(Portal, null = True,
                               on_delete = models.CASCADE)
    def __str__(self):
        return self.title


# Create your models here.
