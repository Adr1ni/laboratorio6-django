from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    lista_categorias = Categoria.objects.all()
    context = {
        'productos':product_list,
        'categorias':lista_categorias
    }
    return render(request,'tienda/index.html', context)

def producto(request,producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'tienda/producto.html', {'producto' : producto})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    producto_categoria = Producto.objects.filter(categoria = categoria)
    return render(request,'tienda/categoria_producto.html', {
        "producto_categoria":producto_categoria,
        "categoria":categoria
    })


