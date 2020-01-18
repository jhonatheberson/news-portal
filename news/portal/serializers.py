from .models import News, Portal
from rest_framework import serializers


class PortalSerializer(serializers.ModelSerializer):
    """
    portal serialization
    """
    class Meta:
        model = Portal  # shows all the bank fields
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    """
    same thing if it were done like that
    title: serializers.CharField()
    portal: serializers.CharField()
    portal = PortalSerializer()
    """
    class Meta:
        model = News
        exclude = ['id']  # excludes what will show (get), also in the input
