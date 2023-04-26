from django.db import models


# Create your models here.
##create the job model: the attributes of the class object make up the info in the database

class Blog(models.Model):
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.CharField()
