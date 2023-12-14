from django.shortcuts import render
from .models import Reciept

def index(request):
    reciepts = Reciept.objects.filter(user=request.user)
    context = {'reciepts': reciepts}
    return render(request, 'reciepts/index.html', context)

def recieptView(request, pk):
    reciept = Reciept.objects.get(id=pk)
    context = {'reciept': reciept}
    return render(request, 'reciepts/reciept.html', context)
