from rest_framework import serializers
from .models import Category, Channel, Creator, CreatorCategory
from django.contrib.auth.models import Group, User

class CreatorCategorySerializer(serializers.ModelSerializer):
  category_name = serializers.ReadOnlyField(source='category.name')

  class Meta:
    model=CreatorCategory
    fields=['id','category', 'category_name', 'added_at']

class ChannelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Channel
    fields = ['id', 'platform', 'url', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Category
    fields=['id', 'name', 'description']

class CreatorSerializer(serializers.ModelSerializer):
  categories = CategorySerializer(many=True, read_only=True)
  channels = ChannelSerializer(many=True, read_only=True)

  class Meta:
    model=Creator
    field=['id', 'name', 'description'  , 'categories', 'channels', 'created_at', 'updated_at' ]

class CreatorWriteSerializer(serializers.ModelSerializer):
  class Meta:
    model=Creator
    fields=['id', 'name', 'description', 'categories']

    def create(self, validated_data):
      categories_data = validated_data.pop('categories', [])
      creator = super().create(validated_data)
      creator.categories.set(categories_data)
      return creator
    
    def update(self, instance, validated_data):
      categories_data = validated_data.pop('categories', [])
      instance = super().update(instance, validated_data)
      instance.categories.set(categories_data)
      return instance
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=User
    fields = ['url', 'username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta :
    model=Group
    fields=['url', 'name']