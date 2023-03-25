from django.contrib import admin
from .models import Post

# Register your models here.
# Registrar el modelo que acabamos de crear 
# Primero hay que importar desde modelos 

admin.site.register(Post)