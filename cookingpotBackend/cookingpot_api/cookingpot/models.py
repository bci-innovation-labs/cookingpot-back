from django.db import models
import jsonfield
# Create your models here.


class FoodRecipe(models.Model):
    name = models.CharField(max_length=20)
    longDescription = models.TextField(max_length=1000)
    ingredients = jsonfield.JSONField()
    tips = models.TextField(max_length=1000)
    foodinstructions = models.CharField(max_length=20)
    shortdescription = models.TextField(max_length=1000)
    user = models.CharField(max_length=20)
