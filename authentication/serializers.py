from rest_framework.schemas.coreapi import serializers


class CredientalsSerializer(serializers.Serializer):
    username = serializers.CharField()
    # leaving it as a character field for now
    password = serializers.CharField()


