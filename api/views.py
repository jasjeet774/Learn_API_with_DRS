from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from api.models import Company,Employee
from api.serializers import  CompanySerializer,EmployeeSerialzer
from rest_framework.response import Response

# Create your views here.
#  viewset is a class-based view that provides a convenient way to define 
# the CRUD (Create, Read, Update, Delete) operations for a model in a concise and consistent manner. 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
#companies/{companyId}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerialzer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists error'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerialzer
