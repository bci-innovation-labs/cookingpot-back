from rest_framework import serializers
from food.models import userDetail

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = userDetail
        fields=('userName')
