from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField

# Model Base
class ModelBase(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default = True)
    datetime_creation = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    datetime_modification = models.DateField('Fecha de modificación', auto_now = True, auto_now_add = False)
    datetime_delete = models.DateField('Fecha de eliminación', auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True 
     
# Categories
class Categorie(ModelBase):
    name = models.CharField('Nombre de la categoria', max_length = 100, unique = True)
    image = models.ImageField('Imágen referencial', upload = 'categories/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


# Users
class User(ModelBase):
    first_name = models.CharField('Nombres', max_length = 100)
    last_name = models.CharField('Apellidos', max_length = 120)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    description = models.TextField('Descripción')
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




# Product
class Product(ModelBase):
    title = models.CharField('titulo del producto', max_length = 150, unique = True)
    sku = models.CharField('titulo del producto', max_length = 150, unique = True)
    description = models.CharField('Descripción')
    content = RichTextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE)
    image = models.ImageField('Imagen referencial', upload_to = 'images/')
    price = models.DecimalField('Precio del producto', max_digits = 1500, decimal_places = 2)
    stars = models.BigIntegerField('Estrellas')
    publicated = models.BooleanField('Publicado / No publicado', default = False)
    datetime_publicated = models.DateField('Fecha de publicación')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title


# App info
class App(ModelBase):
    about = models.TextField('Nosotros')
    phone = models.CharField('Teléfono', max_length = 10)
    email = models.EmailField('Correo electronico', max_length = 200)
    direction = models.CharField('Teléfono', max_length = 10)
    
    class Meta:
        verbose_name = 'Informacion'
        verbose_name_plural = 'Informaciones'

    def __str__(self):
        return self.about

