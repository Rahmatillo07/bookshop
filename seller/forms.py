from django import forms
from manager.models import Book,Category



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category','image','title','description','price','quantity','author','date_created','discount']

        widgets = {
            'category':forms.Select(attrs={
                'class':'form-control'
            }),

            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'price'
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'quantity'
            }),

            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'author'
            }),

            'date_created': forms.DateInput(attrs={
                'class': 'form-control',
            }),

            'discount': forms.Select(attrs={
                'class': 'form-control',
            }),

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'name'
            }),
        }