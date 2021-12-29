from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import serializers
from  rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import PostSerializers
from .models import Post



class TestView(APIView):
    def get(self,request,*args,**kwargs):
        qs = Post.objects.all()
        post= qs.first()
        # serializer = PostSerializers(qs,many =True)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = PostSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# def test_view(request):
#     data = {
#         'name':'john',
#         'age':23
#     }
#     return  JsonResponse(data)