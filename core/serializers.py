from django.db import models
from django.forms import fields
from rest_framework import serializers
from .models import Post


# from django import forms

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'title','description'
#         )


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = (
            'title','description','owner'
        )