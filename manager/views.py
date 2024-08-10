from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import RegisterForm, LoginForm, EditProfileForm, EditUserForm
from .models import Category, User, Book, Cart
from .permissions import AdminRequiredMixin


def home(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).count()
    else:
        cart = 0
    if request.GET != {}:
        books = Book.objects.filter(
            Q(title__icontains=request.GET['search']) | Q(description__icontains=request.GET['search']) | Q(
                author__icontains=request.GET['search']))
    else:
        books = Book.objects.all()
    context = {
        'categories': categories,
        'books': books,
        'cart': cart,
    }
    return render(request, 'manager/index.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'manager/about.html')


def category_by_books(request, category_id):
    categories = Category.objects.all()
    books = Book.objects.filter(category_id=category_id)
    context = {
        'categories': categories,
        'books': books,
    }
    return render(request, 'manager/index.html', context)


class BookDetail(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if request.user.is_authenticated:
            cart_count = Cart.objects.count()
        else:
            cart_count = 0
        return render(request, 'manager/book_detail.html', {'book': book, 'cart_count': cart_count})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST.get('cart'))
        user = request.user
        cart = Cart.objects.filter(user=user, book=book).first()

        if cart:
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart.objects.create(user=user, book=book, quantity=quantity)

        return redirect('manager:home')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'manager/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('manager:home')

        form = LoginForm()

        return render(request, 'manager/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'manager/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('manager:login_page')
        return render(request, 'manager/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = EditProfileForm(instance=request.user)
        return render(request, 'manager/profile.html', {'form': form, 'user': user})


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = EditProfileForm(instance=user)
        return render(request, 'manager/edit_profile.html', {'form': form, 'user': user})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

            return redirect('manager:profile', user_id=user_id)
        form = EditProfileForm()
        return render(request, 'manager/edit_profile.html', {'form': form, 'user': user})


def logout_view(request):
    logout(request)
    return redirect('manager:login_page')


class CartDetail(LoginRequiredMixin, View):
    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        return render(request, 'manager/cart_detail.html', {'carts': carts})


def delete_cart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return redirect('manager:cart_detail')


class DashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'manager/dashboard.html')


class AllUsers(AdminRequiredMixin, View):
    def get(self, request):
        if request.GET != {}:
            users = User.objects.filter(
                Q(first_name__icontains=request.GET['search']) | Q(last_name__icontains=request.GET['search']) | Q(
                    username__icontains=request.GET['search']))
        else:
            users = User.objects.all()

        return render(request, 'manager/all_users.html', {'users': users})


class EditUser(AdminRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = EditUserForm()
        return render(request, 'manager/edit_user.html', {'user': user, 'form': form})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

            return redirect('manager:all_users')

        return render(request, 'manager/edit_user.html', {'user': user, 'form': form})


class DeleteUser(AdminRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return redirect('manager:all_users')


class SellersView(AdminRequiredMixin, View):
    def get(self, request):
        form = EditUserForm()
        sellers = User.objects.filter(user_role='seller')
        return render(request, 'manager/all_sellers.html', {'sellers': sellers, 'form': form})


class AdminsView(AdminRequiredMixin, View):
    def get(self, request):
        admins = User.objects.filter(user_role='admin')
        form = EditUserForm()
        return render(request, 'manager/all_admins.html', {'admins': admins, 'form': form})
