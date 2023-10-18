from rest_framework.views import APIView
from rest_framework.response import Response


from .models import *
from .serializer import *


class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    

class CategoriaView(APIView):
    def get(self,request):
        dataSeries = Categoria.objects.all()
        serSeries = CategoriaSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = CategoriaSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)


class CategoriaDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Categoria.objects.get(pk=serie_id)
        serSerie = CategoriaSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Categoria.objects.get(pk=serie_id)
        serSerie = CategoriaSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Categoria.objects.get(pk=serie_id)
        serSerie = CategoriaSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
    

class ProductoView(APIView):
    def get(self,request):
        dataSeries = Producto.objects.all()
        serSeries = ProductoSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = ProductoSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)


class ProductoDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Producto.objects.get(pk=serie_id)
        serSerie = ProductoSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Producto.objects.get(pk=serie_id)
        serSerie = ProductoSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Producto.objects.get(pk=serie_id)
        serSerie = ProductoSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)