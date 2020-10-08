from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Best_Book
from .forms import *
from .filters import BookFilter
from django.http.response import HttpResponse
# from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse
# Create your views here.

#fonction based views


def books_list(request,*args,**kwargs):
    books = Book.objects.all()
    myfilter = BookFilter(request.GET, queryset=books)
    books = myfilter.qs
    context = {
        'book_list': books,
        'myfilter': myfilter,

    }
    return render(request, 'Books/all_books.html', context)


def index(request,*args,**kwargs):
    books = Book.objects.all()
    myfilter = BookFilter(request.GET, queryset=books)
    books = myfilter.qs
    best_book = Best_Book.objects.all().first()
    context = {
        'books': books,
        'best_book': best_book,
        'myfilter': myfilter,



    }
    return render(request, 'Books/indextest.html', context)


def books_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        'book': book,
    }
    return render(request, 'Books/book_detail.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.user = request.user
            form1.save()
            #TODO: rdirect to book detail
            return redirect('Books:index')
    else:
        form = AddBookForm()

    context = {
        'form': form,
    }
    return render(request, 'Books/addbook.html', context)
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


#CBV
# class IndexView(ListView):
#     model=Book
#     ordering=['-published_at']
#     template_name='books/index.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["best_book"] = Best_Book.objects.all().first()
#         return context
    
# class BookList(ListView):
#     model = Book
#     ordering=['-published_at']
#     template_name='books/all_books.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["myfilter"] = BookFilter(self.request.GET, queryset=self.book_list)
#         return context
    

# class BookDetail(DetailView):
#     model=Book
#     template_name='books/book_detail.html'
    

# class BookCreate(CreateView):
#     model = Book
#     template_name = 'Books/addbook.html'
#     form_class = AddBookForm

#     def form_valid(self, form):
#         form1 = form.save(commit=False)
#         form1.user = self.request.user
#         form1.save()
#         return super().form_valid(form)

# class BookUpdate(UpdateView):
#     model=Book
#     form_class = AddBookForm
#     template_name = 'Books/addbook.html'
#     success_url= 'Books:index'
#     def get_object(self):
#         slug=self.kwargs.get('slug')
#         return get_object_or_404(Book,slug=slug)

#     def form_valid(self, form):
#         return super().form_valid(form)




