from django.shortcuts import get_object_or_404, redirect, render
from .models import Book
from .forms import *
# Create your views here.

def index(request):
    books=Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'Books/index.html',context)
def add_book(request):
    if request.method=='POST':
        form=AddBookForm(request.Post,request.FILES)
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
