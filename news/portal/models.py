from django.db import models


class Portal(models.Model):
    """
    medel of the database table that was created
    this table refers to table News
    """
    name = models.CharField(max_length=40)  # name of the news portal or url

    def __str__(self):
        return self.name


class News(models.Model):
    """
    medel of the database table that was created
    """
    title = models.CharField(max_length=200)  # title of the news
    portal = models.ForeignKey(Portal, null=True,
                               on_delete=models.CASCADE)  # portal of the news
    create_at = models.DateTimeField(
        auto_now_add=True)  # good database practice
    update_at = models.DateTimeField(auto_now=True)  # good database practice

    def __str__(self):
        return self.title

# Create your models here.
