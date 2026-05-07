from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        empty_label=None,
        queryset=Author.objects.all(),
        required=True,
        label="Author",
        widget=forms.Select(attrs={
            'class': 'mycssclass',
            'id': 'jsID2'
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating']
        widgets = {
            'pubdate': forms.DateInput(attrs={'type': 'date'}),
        }
