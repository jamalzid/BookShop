from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from .filters import BookFilter
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    books=Book.objects.all()
    myfilter=BookFilter(request.GET,queryset=books)
    books=myfilter.qs
    best_book = Best_Book.objects.all().first()
    context = {
        'books': books,
        'best_book': best_book,
        'myfilter': myfilter,



    }
    return render(request,'Books/indextest.html',context)

def books_list(request):
    books = Book.objects.all()
    myfilter = BookFilter(request.GET, queryset=books)
    books = myfilter.qs
    context = {
        'books': books,
        'myfilter': myfilter,

    }
    return render(request, 'Books/all_books.html', context)

def add_book(request):
    if request.method=='POST':
        form=AddBookForm(request.POST,request.FILES)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.user=request.user
            form1.save()
            #TODO: rdirect to book detail
            return redirect('Books:index')
    else:
        form = AddBookForm()


    context = {
        'form': form,
    }
    return render(request,'Books/addbook.html',context)
def books_detail(request,slug):
    book=get_object_or_404(Book,slug=slug)
    context = {
        'book': book,
    }
    return render(request, 'Books/book_detail.html', context)


def update_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            #TODO: rdirect to book detail
            return redirect('Books:index')
    else:
        form = AddBookForm(instance=book)

    context = {
        'book': book,
        'form': form,

    }
    return render(request, 'Books/book_update.html', context)


def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.user == book.user:
        book.delete()
    return redirect('Books:index')    
