from django.db import models

# Create your models here.


class User(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.fname+" "+self.lname)
