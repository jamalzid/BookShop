from django.urls import path, include
from . import views as v
app_name='Books'
urlpatterns = [
    path('add-book/', v.add_book, name='add_book'),
   path('all-books/', v.books_list, name='books_list'),

   
   path('', v.index, name='index'),
    path('<slug:slug>/', v.books_detail, name='books_detail'),
    path('<slug:slug>/update', v.update_book, name='update_book'),
   path('<slug:slug>/delete', v.delete_book, name='delete_book'),

]
