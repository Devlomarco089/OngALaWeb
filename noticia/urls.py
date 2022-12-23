from django.urls import path
from .views import HomeView, CategoriaView, ArticuloDetailView, ComentarioForm

urlpatterns = [ 
    path('', HomeView.as_view(), name="home"),
    path('', CategoriaView.as_view()),
    path('articulo/<int:pk>', ArticuloDetailView.as_view(), name="articulo"),
    path('articulo/<int:pk>/addcoment', ComentarioForm.as_view(), name="comentar"),
]