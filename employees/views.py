from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import *
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#authentications

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

#CRUD operations

@api_view(['GET'])
def getAllEmployees(request):
    permission_classes = [permissions.IsAuthenticated]
    queryset= Employee.objects.all()
    serializers = EmployeeSerializer(queryset,many=True)
    return Response({
        "data":serializers.data
    })


@api_view(['POST'])
def createEmployee(request):
    permission_classes = [permissions.IsAuthenticated]
    serializers = EmployeeSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response("Employee Added successfully",status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateEmployee(request,pk):
    permission_classes = [permissions.IsAuthenticated]
    try:
        presentEmployee= Employee.objects.get(pk=pk)
        serializers = EmployeeSerializer(presentEmployee,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("Updated Successfully",status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response("Employee not exist with given id",status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteEmployee(request,pk):
    permission_classes = [permissions.IsAuthenticated]
    try:
        presentEmployee= Employee.objects.get(pk=pk)
        presentEmployee.delete()
        return Response("Deleted Successfully",status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response("Employee not exist with given id",status=status.HTTP_404_NOT_FOUND)