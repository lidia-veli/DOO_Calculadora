from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))

    
    if request.GET.get('sumar') == "":
        ans = num1 + num2

    elif request.GET.get('restar') == "":    
        ans = num1 - num2

    elif request.GET.get('multiplicar') == "":    
        ans = num1 * num2

    elif request.GET.get('dividir') == "":
        if num2 == 0:
            ans = "No se puede dividir entre 0"    
        ans = num1 * num2

    
    return render(request, 'result.html', {'ans': ans})