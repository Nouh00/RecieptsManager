from django.shortcuts import render, redirect
from .models import Reciept
from .forms import ReceiptForm

def index(request):
    reciepts = Reciept.objects.filter(user=request.user)
    context = {'reciepts': reciepts}
    return render(request, 'reciepts/index.html', context)

def recieptView(request, pk):
    reciept = Reciept.objects.filter(id=pk)[0]
    context = {'reciept': reciept}
    return render(request, 'reciepts/reciept.html', context)

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