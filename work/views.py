from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from work.models import Position, Employee
from work.serializers import PositionSerializer, EmployeeSerializer


class PositionAPIView(APIView):
    def get(self, request):
        p = Position.objects.all()
        serializers = PositionSerializer(p, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = PositionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)


class EmployeeAPIVIew(APIView):
    def get(self, request):
        p = Employee.objects.all()
        serializers = EmployeeSerializer(p, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
