from django.urls import path, include
from . import views as v
app_name='Books'
urlpatterns = [
   path('add-book/', v.add_book, name='add_book'),
   path('',v.index,name='index'),
   path('<slug:slug>/', v.books_detail, name='books_detail'),

   

]
