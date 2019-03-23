from rest_framework import serializers
from django.contrib.auth.models import User

from holders.models import Meal, DishType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'receipt_id', 'customer', 'ordered_at')


class DishTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DishType
        fields = ('name', 'slug')
