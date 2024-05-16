from rest_framework import serializers

from .models import student

class strudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    city = serializers.CharField(max_length=200)
    rollno = serializers.IntegerField()

    def create(self, validated_data):
        return student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.city= validated_data.get('city', instance.city)
        instance.rollno=validated_data.get('rollno', instance.rollno)
        instance.save()
        return instance


