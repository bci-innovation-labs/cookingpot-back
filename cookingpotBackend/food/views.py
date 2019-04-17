from django.shortcuts import render


from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from food.models import userDetail
from food.serializers import userSerializer

class userList(APIView):
    def get(self,request):
        user1= userDetail.object.all()
        serializer= userSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
