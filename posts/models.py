from django.db import models

# Create your models here.
# Por cada cosa que hagamos en models tenemos que hacer una migracion 
# python manage.py makemigrations 

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
        # mostrar desde el principio hasta el caracter 50
