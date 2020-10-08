
from django.db import models
from django_countries.fields import CountryField  
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Category(models.Model):
        title = models.CharField(max_length=50)
        def __str__(self):
            return self.title



class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='books-images/')
    price=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=100,default='not defined')
    published_at=models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    

    def __str__(self):
            return self.title

    def get_absolute_url(self):  # new
        return reverse('Books:books_detail', args=[str(self.slug)])
        
    @property
    def days_since_published(self):
        days = timezone.now()-self.published_at
        return days.days
class Best_Book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title
