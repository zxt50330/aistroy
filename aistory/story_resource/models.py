from django.db import models

# Create your models here.


class ModelBase(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Resource(ModelBase):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200)
