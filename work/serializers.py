from rest_framework import serializers

from work.models import Position, Employee


class PositionSerializer(serializers.Serializer):
    positions = serializers.CharField()
    departament = serializers.CharField()

    def create(self, validated_data):
        return Position.objects.create(**validated_data)


class EmployeeSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    birth_year = serializers.DateField()
    departament_id = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
