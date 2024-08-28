from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import *
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
def getAllEmployees(request):
    queryset= Employee.objects.all()
    serializers = EmployeeSerializer(queryset,many=True)
    return Response({
        "data":serializers.data
    })


@api_view(['POST'])
def createEmployee(request):
    serializers = EmployeeSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response("Employee Added successfully",status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateEmployee(request,pk):
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
    try:
        presentEmployee= Employee.objects.get(pk=pk)
        presentEmployee.delete()
        return Response("Deleted Successfully",status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response("Employee not exist with given id",status=status.HTTP_404_NOT_FOUND)