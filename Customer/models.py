from django.db import models
from Evaluator.models import Evaluator
from MyAdmin.models import User
# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    url = models.CharField(max_length=255,null=True, blank=True)
    webName=models.CharField(max_length=255,null=True, blank=True)
    desc= models.TextField(null=True, blank=True)
    assigned_evaluator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
'''
class URL(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url
'''