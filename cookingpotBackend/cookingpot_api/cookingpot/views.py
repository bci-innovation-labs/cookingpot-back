from django.shortcuts import render
from rest_framework import viewsets
from .models import FoodRecipe
from .serializers import FoodRecipeSerializers
# Create your views here.

class FoodRecipeView(viewsets.ModelViewSet):
    queryset = FoodRecipe.objects.all();
    serializer_class = FoodRecipeSerializers
