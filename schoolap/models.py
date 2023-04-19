from django.db import models

# Create your models here.


class Clas(models.Model):
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=100)
    images = models.ImageField(upload_to='image',blank=True,null=True)
    table = models.CharField(max_length=500)
    teacher = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class ClasSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book