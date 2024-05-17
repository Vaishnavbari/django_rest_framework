from django.shortcuts import render
from .models import employee
from .serializer import employee_serializer
from rest_framework import viewsets
from rest_framework.response import Response
"""
ViewSet Class
A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as get() or post(), and instead provides actions such as list() and create().

• list() - Get All Records.
• retrieve() – Get Single Record
• create() - Create/Insert Record
• update() - Update Record Completely
• partial_update() – Update Record Partially 
• destroy() - Delete Record 

""" 

"""
>>> Methods <<<
ViewSet Class
from rest_framework import viewsets
class StudentViewSet(viewsets.ViewSet):
def list(self, request):
    pass
def create(self, request):
    pass
def retrieve(self, request, pk=None):
    pass
def update(self, request, pk=None):
    pass
def partial_update(self, request, pk=None):
    pass
def destroy(self, request, pk=None)
    pass
"""


class employee_viewset(viewsets.ViewSet):
    
     def list(self,request):
        emp=employee.objects.all()
        serializer_data=employee_serializer(emp,many=True)

        return Response(serializer_data.data)
     
     def create(self, request):
          serializer_data=employee_serializer(data=request.data)
          if serializer_data.is_valid():
              serializer_data.save()
          return Response("data saved successfully")
     
     def retrieve(self, request, pk=None):
        user=employee.objects.filter(id=pk).first()
        serializer_data=employee_serializer(user)
        return Response(serializer_data.data)
     
     def update(self, request, pk=None):
        user=employee.objects.filter(id=pk).first()
        serializer_data=employee_serializer(instance=user,data=request.data)
        if serializer_data.is_valid():
              serializer_data.save()
        
        return Response("user update sucessfully")
     
     def partial_update(self, request, pk=None):
        user=employee.objects.filter(id=pk).first()
        serializer_data=employee_serializer(instance=user,data=request.data)
        if serializer_data.is_valid():
              serializer_data.save()
        return Response("user update sucessfully")
     
     def destroy(self, request, pk=None):
        user=employee.objects.filter(id=pk).first()
        user.delete()
        return Response("user deleted sucessfully")
     
     

class employeemodel_viewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employee_serializer



class employee_readonly_model_viewset(viewsets.ReadOnlyModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employee_serializer
