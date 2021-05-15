"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="Welcome"),
    path('save_book/',views.save_book),
    path('edit_book/<int:id>/', views.edit_book),
    path('delete_book/<int:pk>/', views.delete_book),
    path('Show_deleted_data/', views.show_deleted_data),
    path('permanant_delete_book/<int:pk>/', views.permanant_delete_book),
    path('restore/<int:id>/', views.restore_book),
    path('delete_all/', views.delete_all),
    path('restore_all/', views.restore_all),
]


#http://127.0.0.1:8000/ base url for admin

