from rest_framework import serializers
from languages.models import Language


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('url', 'id', 'name', 'paradigm')
