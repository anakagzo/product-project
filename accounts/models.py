from django.db import models


# Create your models here.
class Acc(models.Model):
    icon = models.FileField(upload_to='images/')
    image = models.FileField(upload_to='images/')
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.CharField()
    url=models.URLField()
