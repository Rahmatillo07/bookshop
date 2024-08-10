from django.urls import path
from .views import (home,category_by_books,BookDetail,LoginView,logout_view,RegisterView,ProfileView,EditProfileView,
                    CartDetail,delete_cart,DashboardView,AboutView,EditUser,DeleteUser,SellersView,AllUsers,AdminsView)

app_name = 'manager'

urlpatterns = [
    path('',home,name='home'),
    path('category-by-books/<int:category_id>/',category_by_books,name='category'),
    path('book-detail/<int:book_id>/',BookDetail.as_view(),name='book_detail'),
    path('login-page/',LoginView.as_view(),name='login_page'),
    path('logout/',logout_view,name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/<int:user_id>/',ProfileView.as_view(),name='profile'),
    path('edit-profile/<int:user_id>/',EditProfileView.as_view(),name='edit_profile'),
    path('cart-detail/',CartDetail.as_view(),name='cart_detail'),
    path('delete-cart/<int:cart_id>/',delete_cart,name='delete_cart'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('about/',AboutView.as_view(),name='about'),
    path('edit-user/<int:user_id>/',EditUser.as_view(),name='edit_user'),
    path('delete-user/<int:user_id>/',DeleteUser.as_view(), name='delete_user'),
    path('all-sellers/',SellersView.as_view(),name='all_sellers'),
    path('all-users/',AllUsers.as_view(),name='all_users'),
    path('all-admins/',AdminsView.as_view(),name='all_admins'),

]