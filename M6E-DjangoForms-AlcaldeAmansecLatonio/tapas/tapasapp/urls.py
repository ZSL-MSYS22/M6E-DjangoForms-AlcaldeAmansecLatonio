# Johann Miguel S. Alcalde, 240150 ; Samantha Louise F. Amansec, 230286 ; Zale Sebastian S. Latonio, 242494
'''
We hereby attest to the truth of the following facts:

We have not discussed the Python code in our program with anyone
other than my instructor or the teaching assistants assigned to this course.

We have not used Python code obtained from another student, or
any other unauthorized source, whether modified or unmodified.

If any Python code or documentation used in our program was
obtained from another source, it has been clearly noted with citations in the
comments of our program.'''

from django.urls import path
from . import views


urlpatterns = [
    # 4.a.i Loads at localhost:8000/
    path('', views.login, name='login'),
    # path(‘pattern_name/<param_type: name_of_param>’, views.function, name=’reference_name’)

    path('better_menu', views.better_menu, name='better_menu'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:pk>/', views.update_dish, name='update_dish'),

    path('error_page', views.error_page, name='error_page'),
]