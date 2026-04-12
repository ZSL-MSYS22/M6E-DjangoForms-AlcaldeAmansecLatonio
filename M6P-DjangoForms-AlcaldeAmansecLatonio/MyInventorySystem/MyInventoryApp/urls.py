"""
URL configuration for MyInventorySystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('view_suppliers/', views.view_suppliers, name='view_suppliers'),
    path('view_water_bottles/', views.view_water_bottles, name='view_water_bottles'),
    path('add_bottle/', views.add_bottle, name='add_bottle'),
    path('view_bottle_details/<int:pk>/', views.view_bottle_details, name='view_bottle_details'),
    path('delete_bottle/<int:pk>/', views.delete_bottle, name='delete_bottle'),
    path('manage_account/', views.manage_account, name='manage_account'),
    path("change_password/", views.change_password, name="change_password"),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_view, name='logout'),
]
