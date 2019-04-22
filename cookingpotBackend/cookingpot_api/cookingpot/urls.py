from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('foodrecipe',views.FoodRecipeView)


urlpatterns = [
  path('', include(router.urls))
]
