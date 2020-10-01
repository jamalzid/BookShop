from django import forms
from .models import Book,Author
class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields='__all__'
        exclude=('user',)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ('added_by',)
