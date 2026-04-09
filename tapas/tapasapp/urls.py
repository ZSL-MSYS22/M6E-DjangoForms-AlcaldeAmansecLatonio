from django.urls import path
from . import views


urlpatterns = [
    # 4.a.i Loads at localhost:8000/
    path('', views.add_menu, name='add_menu'),
    # path(‘pattern_name/<param_type: name_of_param>’, views.function, name=’reference_name’)

    path('better_menu', views.better_menu, name='better_menu'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:pk>/', views.update_dish, name='update_dish'),
]