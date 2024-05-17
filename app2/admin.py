from django.contrib import admin

from .models import employee 
# Register your models here.
@admin.register(employee)
class employeeadmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
        
