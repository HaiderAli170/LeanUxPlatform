from django.db import models
from django.db import models




class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_position = models.CharField(max_length=100)