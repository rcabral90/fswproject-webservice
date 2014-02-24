from com_fsw_service.models import Diet, AuthUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('id', 'username')


class DietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diet
        fields = ('diet_id', 'resident_id', 'diet_title', 'diet_description')