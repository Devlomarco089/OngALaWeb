from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Noticia, Categoria, Comentario
from django.urls import reverse_lazy
from .forms import ComentarioForm

class HomeView(ListView):
    model = Noticia
    template_name = 'index.html'
    ordering = ['-publicado']

class CategoriaView(ListView):
    model = Categoria
    template_name = 'index.html'

class ArticuloDetailView(DetailView):
    model = Noticia
    template_name = 'articulo.html'

class ComentarioForm(CreateView):
    model = Comentario
    # form_class = ComentarioForm
    fields = '__all__'
    template_name = 'addcoment.html'
    # # def form_valid(self, form):
    # #     form.instance.post_id = self.kwargs['fk']
    # #     return super().form_valid(form)

    success_url = reverse_lazy('home')



