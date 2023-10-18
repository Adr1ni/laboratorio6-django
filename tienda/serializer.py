from rest_framework import serializers
from .models import *


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'categoria', 'nombre', 'precio', 'stock','pub_date')
        

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre','pub_date')