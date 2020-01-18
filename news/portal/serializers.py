from .models import News, Portal
from rest_framework import serializers


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    # como vai ser os arquivos para API
    # title: serializers.CharField()
    # portal: serializers.CharField()
    # portal = PortalSerializer()

    class Meta:
        model = News
        # fields = '__all__' # mostra tudos os campos do banco
        exclude = ['id']  # exclui o que vai mostrar, também no input
