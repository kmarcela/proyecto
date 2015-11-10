from django.shortcuts import render

def vertienda(request):
    return render(request, 'tienda/vertienda.html', {})
