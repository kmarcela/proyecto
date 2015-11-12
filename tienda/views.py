from django.shortcuts import render, get_object_or_404
from .models import venta
from .forms import Pubform

def vertienda(request):
    ventas = venta.objects.all().order_by('precio')
    return render(request, 'tienda/vertienda.html', {'posts': ventas})

def detalleproducto(request, pk):
    post = get_object_or_404(venta, pk=pk)
    return render(request, 'tienda/detalleproducto.html', {'post': post})

def nuevaventa(request):
    if request.method == "POST":
        form = Pubform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.producto = request.producto
            post.save()
            return redirect('tienda.views.detalleproducto', pk=post.pk)
    else:
        form = Pubform()
    return render(request, 'tienda/nuevaventa.html', {'form': form})
