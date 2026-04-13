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

# Creating Data Records (Code Perspective)

def login(request):

    if(request.method=="POST"):
        username = request.POST.get('username') 
        password = request.POST.get('password')
        
        if username=="" or password=="":
            loginMessage = 'Please input username and password.'
            # https://docs.djangoproject.com/en/6.0/ref/contrib/messages/
            return render(request, 'tapasapp/login_page.html', {'message':loginMessage})
        
        account = Account.objects.filter(username=username).first()        
        # Returns the first object matched by the queryset, or None if there is no matching object
        # https://docs.djangoproject.com/en/6.0/ref/models/querysets/

        if account != None and password == account.password:
            return redirect('basic_list', pk=account.pk)
            # https://www.geeksforgeeks.org/python/django-return-redirect-with-parameters/
        else:
            loginMessage = 'Invalid Login'
            # https://docs.djangoproject.com/en/6.0/ref/contrib/messages/
            return render(request, 'tapasapp/login_page.html', {'message':loginMessage})

    else:
        return render(request, 'tapasapp/login_page.html')


def sign_up(request):
    global signUpMessage

    if(request.method=="POST"):
        username = request.POST.get('username') 
        password = request.POST.get('password')

        if not username or not password:
            signUpMessage = 'Please enter a username and password'
            return render(request, 'tapasapp/sign_up_page.html', {'message':signUpMessage})
    
        account = Account.objects.filter(username=username).first()

        if account != None:
            signUpMessage = 'Account already exists'
            return render(request, 'tapasapp/sign_up_page.html', {'message':signUpMessage})
        else:
            Account.objects.create(username=username, password=password)
            return redirect('login')

    else:
        return render(request, 'tapasapp/sign_up_page.html')

def basic_list(request, pk):
    account = Account.objects.get(pk=pk)
    return render(request, 'tapasapp/basic_list.html', {'pk':pk, 'account':account})

def manage_account(request, pk):
    account = Account.objects.get(pk=pk)
    return render(request, 'tapasapp/manage_account.html', {'pk':pk, 'account':account})

def delete_account(request, pk):
    Account.objects.get(pk=pk).delete()
    return redirect('login')

# WIP
def change_password(request,pk):
    if(request.method=='POST'):
        currentPassword = request.POST.get('currentPassword')
        newPassword = request.POST.get('newPassword')
        newPasswordAgain = request.POST.get('newPasswordAgain')

        account = Account.objects.get(pk=pk)

        if currentPassword == account.password:
            if newPassword == newPasswordAgain:
                Account.objects.filter(pk=pk).update(password=newPassword)
                return redirect('manage_account', pk=pk)
            else:
                changePasswordMessage = 'New passwords do not match'
                return render(request, 'tapasapp/change_password.html', {'pk':pk}, {'message':changePasswordMessage})
        else:
            changePasswordMessage = 'Incorrect current password'
            return render(request, 'tapasapp/change_password.html', {'pk':pk}, {'message':changePasswordMessage})

    else:
        return render(request, 'tapasapp/change_password.html', {'pk':pk})

    return render(request, 'tapasapp/change_password.html', {'pk':pk})