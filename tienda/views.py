from django.shortcuts import render, get_object_or_404
from .models import venta

def vertienda(request):
    ventas = venta.objects.all().order_by('precio')
    return render(request, 'tienda/vertienda.html', {'posts': ventas})

def detalleproducto(request, pk):
    post = get_object_or_404(venta, pk=pk)
    return render(request, 'tienda/detalleproducto.html', {'post': post})
