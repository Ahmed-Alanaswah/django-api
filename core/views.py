from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import serializers
from  rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import PostSerializers
from .models import Post
from  rest_framework import generics
# class TestView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self,request,*args,**kwargs):
#         qs = Post.objects.all()
#         post= qs.first()
#         # serializer = PostSerializers(qs,many =True)
#         serializer = PostSerializers(post)
#         return Response(serializer.data)

#     def post(self,request,*args,**kwargs):
#         serializer = PostSerializers(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class PostView(mixins.ListModelMixin,mixins.CreateModelMixin ,generics.GenericAPIView):
    serializer_class= PostSerializers
    queryset=Post.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class= PostSerializers
    queryset=Post.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PostListCreateview(generics.ListCreateAPIView):
    serializer_class= PostSerializers
    queryset=Post.objects.all()
    


