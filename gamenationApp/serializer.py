from rest_framework import serializers


class TrafficSourceSerializer(serializers.Serializer):
    excel = serializers.FileField()
