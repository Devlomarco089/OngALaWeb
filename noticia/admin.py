from django.contrib import admin
from .models import Noticia, Categoria, Comentario

admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)
