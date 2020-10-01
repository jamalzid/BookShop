from django.db import models
from django_countries.fields import CountryField  
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
        title = models.CharField(max_length=50)
        def __str__(self):
            return self.title

class Author(models.Model):
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.full_name

    

class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='books-images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_at=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
            return self.title
    
