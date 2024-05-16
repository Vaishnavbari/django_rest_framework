from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import student
from .serializers import strudentSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,RetrieveModelMixin

# Function based view 
@csrf_exempt
@api_view(["GET","POST","PUT","DELETE"])
def api_flow(request,id=None):

    if request.method=="POST":
        serializer = strudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully"}, status=201)
        return Response({"error": serializer.errors}, status=400)
    
    if request.method=="PUT":
        if id is not None:
            user=student.objects.get(id=id)
            serializer = strudentSerializer(instance=user,data=request.data,partial=True)  
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Data updated successfully"}, status=201)
        return Response({"error": serializer.errors}, status=400)
    
    if request.method=="DELETE":
        user=student.objects.get(id=id)
        user.delete()
        return Response({"message": "user deleted successfully"}, status=201)
    
    data = student.objects.all()
    if id is not None:
         data = student.objects.get(id=id)
         serializer = strudentSerializer(data)
         return Response({"data": serializer.data})
         
    serializer = strudentSerializer(data, many=True)
    return Response({"data": serializer.data})


# class based view 
class students(APIView):
    def get(self,request,id=None):
        data = student.objects.all()
        if id is not None:
            data = student.objects.get(id=id)
            serializer = strudentSerializer(data)
            return Response({"data": serializer.data})
            
        serializer = strudentSerializer(data, many=True)
        return Response({"data": serializer.data})
    def post(self, request,id=None):
        serializer = strudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully"}, status=201)
        return Response({"error": serializer.errors}, status=400)
    
    def put(self, request, id=None):
        if id is not None:
            user=student.objects.get(id=id)
            serializer = strudentSerializer(instance=user,data=request.data,partial=True)  
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Data updated successfully"}, status=201)
        return Response({"error": serializer.errors}, status=400)
    
    def patch(self, request, id=None):
        if id is not None:
            user=student.objects.get(id=id)
            serializer = strudentSerializer(instance=user,data=request.data,partial=True)  
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Data updated successfully"}, status=201)
        return Response({"error": serializer.errors}, status=400)
    
    def delete(self, request, id=None):
        if id is not None:
         user = student.objects.get(id=id)
         user.delete()
         return Response({"data":"user deleted"})
        
# Genericapiview and Mixins 

class student_genericapi(GenericAPIView,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=strudentSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    


class student_genericapi_toget(GenericAPIView,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=strudentSerializer
    
    def put(self,request,*args, **kwargs):
        return self.update(request)
     
    def get(self,request,*args, **kwargs):
       return self.retrieve(request)
    
    def delete(self,request,*args, **kwargs):
       return self.delete(request)
    


# create api view and retrieveupdateapiview
class create_operation(CreateAPIView):
    queryset=student.objects.all()
    serializer_class=strudentSerializer

class crud_operation(RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=strudentSerializer
