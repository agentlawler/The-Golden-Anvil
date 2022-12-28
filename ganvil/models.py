from django.db import models

# Create your models here.

class User(models.Model):
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    username = models.CharField(max_length=50, null=False, blank = False)
    password = models.CharField(max_length=50, null=False, blank = False)
    name = models.TextField(max_length=50, null=False, blank = False)
    email = models.EmailField(max_length=75, null=False, blank = False)

    def __str__(self):
        return self.username