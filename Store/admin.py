from django.contrib import admin

from Store.models import Categoria, Departamento, Produto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Produto)