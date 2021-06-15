from django.db import models

# Create your models here.
class Create_Model(models.Model):

    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    choices=(("Malyala","Malayalm"),("Englis","English"),("Hind","Hindi"),("Unknown_Lang","Unknown_Lang"))
    language=models.CharField(choices=choices,max_length=50,default="Unknown_Lang")
    pages=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
