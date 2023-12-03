from django.shortcuts import render
from api.models import Bank,Employee
from api.serializers import BankSerializer,EmployeeSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response




# Create your views here.
class Bankviewset(viewsets.ModelViewSet):
    queryset= Bank.objects.all()
    serializer_class=BankSerializer

    @action(detail=True,methods=['get'])

    def employee(self,request,pk=None):

        bank=Bank.objects.get(pk=pk)
        emps=Employee.objects.filter(bank=bank)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        return Response(emps_serializer.data)
        pass
    


class Employeeviewset(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer
