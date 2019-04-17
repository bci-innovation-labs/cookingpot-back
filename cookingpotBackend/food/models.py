from __future__ import unicode_literals

from django.db import models

class userDetail(models.Model):
    userName=models.CharField(max_length=10)
    userEmail=models.CharField(max_length=20)
    userPassword=models.IntegerField()

    def __str__(self):
        return self.userName
