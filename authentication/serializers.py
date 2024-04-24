from rest_framework.schemas.coreapi import serializers


# TODO: Change into a user serializer
class CredientalsSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


