from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect('account:regsuccessful')

        else:
            return redirect('account:regsuccessful')
            
   

    context = {

        'form' : UserCreationForm()

    }
    return render(request, 'account/register.html', context)




def regsuccessful(request):
    return render(request, 'account/reg_successful.html')

def login(request):
    return render(request, 'account/login.html', )

def logout(request):
    return render(request, 'account/logout.html', )

