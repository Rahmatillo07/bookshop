from django.shortcuts import render, redirect,get_object_or_404
from django.views import View

from manager.models import Book,Category
from manager.permissions import SellerRequiredMixin
from .forms import BookForm,CategoryForm





class SellerDashboard(SellerRequiredMixin,View):
    def get(self,request):
        books = Book.objects.all()
        return render(request,'seller/dashboard.html',{'books':books})


class CreateBook(SellerRequiredMixin,View):
    def get(self,request):
        form = BookForm()
        return render(request,'seller/create_book.html',{'form':form})

    def post(self,request):
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return redirect('seller:dashboard')

        return render(request,'seller/create_book.html',{'form':form})


def delete_book(request,book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("seller:dashboard")



class EditBook(SellerRequiredMixin,View):
    def get(self,request,book_id):
        book = Book.objects.get(pk=book_id)
        form = BookForm(instance=book)
        return render(request,'seller/edit_book.html',{'form':form})

    def post(self,request,book_id):
        book = get_object_or_404(Book,pk=book_id)
        form = BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('seller:dashboard')

        return render(request,'seller/edit_book.html',{'form':form})


class CategoriesView(SellerRequiredMixin,View):
    def get(self,request):
        categories = Category.objects.all()
        return render(request,'seller/all_categories.html',{'categories':categories})

class CreateCategory(SellerRequiredMixin,View):
    def get(self,request):
        form = CategoryForm()
        return render(request,'seller/create_category.html',{'form':form})

    def post(self,request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller:all_categories')
        return render(request,'seller/create_category.html',{'form':form})


class EditCategory(SellerRequiredMixin,View):
    def get(self,request,category_id):
        category = get_object_or_404(Category,pk=category_id)
        form = CategoryForm(instance=category)
        return render(request,'seller/edit_category.html',{'form':form})

    def post(self,request,category_id):
        category = get_object_or_404(Category,pk=category_id)
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('seller:all_categories')
        return render(request,'seller/edit_category.html')

def delete_category(request,category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('seller:all_categories')
