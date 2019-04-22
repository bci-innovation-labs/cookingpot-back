from rest_framework import serializers
from .models import FoodRecipe


class FoodRecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = ('id','name','longdescription','ingredients','tips','foodinstructions','shortdescription','users')
