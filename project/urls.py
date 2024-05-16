"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Function based url
    path("student/",views.api_flow),
    path("student/<int:id>",views.api_flow),

    # class based url 
    path("student_class/",views.students.as_view()),
    path("student_class/<int:id>",views.students.as_view()),

    # Generic apiview 

    path("stundent_generic_view/",views.student_genericapi.as_view()),
    path("stundent_generic_view/<int:pk>",views.student_genericapi_toget.as_view()),

    # crud in one operation
    path("crud/",views.create_operation.as_view()),
    path("read_update_delete/<int:pk>",views.crud_operation.as_view()),
]
