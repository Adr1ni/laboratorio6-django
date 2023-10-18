from django.urls import path
from tienda import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('categoria',views.CategoriaView.as_view(),name='categorias'),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),

    path('producto',views.ProductoView.as_view(),name='productos'),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
]