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

from django.shortcuts import render, redirect, get_object_or_404
from .models import Account 
from django.contrib import messages
# https://docs.djangoproject.com/en/6.0/ref/contrib/messages/

# Create your views here.


def better_menu(request):
    account_info = Account.objects.all()
    return render(request, 'tapasapp/better_list.html', {'account_info':account_info})

    '''dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/better_list.html', {'dishes':dish_objects})'''

# Creating Data Records (Code Perspective)
def add_menu(request):
    if(request.method=="POST"):
        username = request.POST.get('username') 
        password = request.POST.get('password')
        usernameCheck = get_object_or_404(Account, username=username)
        passwordCheck = get_object_or_404(Account, password=passoword)
    
        # if username == usernameCheck and password == passwordCheck:
        #     return redirect('better_menu')
        # else:
        #     messages.error(request, 'Invalid Login')
        #     return render(request, 'tapasapp/add_menu.html')

    else:
        return render(request, 'tapasapp/add_menu.html')

    '''if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu')
    else:
        return render(request, 'tapasapp/add_menu.html')'''

def view_detail(request, pk):
    d = get_object_or_404(Dish, pk=pk)
    return render(request, 'tapasapp/view_detail.html', {'d': d})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('better_menu')

def update_dish(request, pk):
    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', pk=pk)
    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_menu.html', {'d':d})