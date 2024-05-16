from django.contrib import admin
from .models import student,Member

# Register your models here.
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=['id',"name","rollno","city"]


@admin.register(Member)
class memeberadmin(admin.ModelAdmin):
    list_display=["firstname","lastname"]


