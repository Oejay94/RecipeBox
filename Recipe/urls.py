"""Recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Recipe import views
from Recipe.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('author/<int:id>/', views.author, name='author'),
    path('addrecipe/', views.add_recipe, name='addrecipe'),
    path('addauthor/', views.add_author, name='addauthor')
]
