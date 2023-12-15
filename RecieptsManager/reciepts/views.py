from django.shortcuts import render, redirect
from .models import Reciept
from .forms import ReceiptForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


#view Reciepts
@login_required(login_url='reciepts:login')
def index(request):
    reciepts = Reciept.objects.filter(user=request.user)
    context = {'reciepts': reciepts}
    return render(request, 'reciepts/index.html', context)

#single Reciept View
def recieptView(request, pk):
    reciept = Reciept.objects.filter(id=pk)[0]
    context = {'reciept': reciept}
    return render(request, 'reciepts/reciept.html', context)

#Reciept CRUD
def newReciept(request):
    print(request.POST)
    form = ReceiptForm(request.POST or None)
    if form.is_valid():
        reciept = form.save(commit=False)
        reciept.user = request.user
        reciept.save()
        return redirect('reciepts:index')
    
    return render(request, 'reciepts/new_reciept.html', {'form': form})

def editReciept(request, pk):
    receipt = Reciept.objects.get(id=pk)
    form = ReceiptForm(request.POST or None, instance=receipt)
    if form.is_valid():
        receipt = form.save(commit=False)
        receipt.user = request.user
        receipt.save()
        return redirect('reciepts:index')
    return render(request, 'reciepts/edit_reciept.html', {'form': form})


def deleteReciept(request, pk):
    receipt = Reciept.objects.get(id=pk)
    receipt.delete()
    return redirect('reciepts:index')

#Authentication

##login and register vieww
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('reciepts:index')
    user_creation_form = UserCreationForm()
    user_login_form = AuthenticationForm()

    if request.method == "POST":
        user_login_form = AuthenticationForm(data=request.POST)
        if user_login_form.is_valid():
            user = user_login_form.get_user()
            if user:
                login(request, user)
                return redirect('reciepts:index')
            return redirect('reciepts:login')
        
    context = {
        'user_creation_form': user_creation_form, 
        'user_login_form': user_login_form
        }
    return render(request, 'reciepts/login.html', context)

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('reciepts:index')
    
    user_creation_form = UserCreationForm()

    if request.method == "POST":
        user_creation_form = UserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            if user:
                login(request, user)
                return redirect('reciepts:index')
            return redirect('reciepts:login')
        
    context = {
        'user_creation_form': user_creation_form, 
        }
    return render(request, 'reciepts/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('reciepts:login')

