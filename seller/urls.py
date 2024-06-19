from django.urls import path
from manager.views import home
from .views import SellerDashboard,CreateBook,delete_book,EditBook,CategoriesView,CreateCategory,EditCategory,delete_category

app_name = 'seller'

urlpatterns = [
    path('',home,name='home'),
    path('dashboard/',SellerDashboard.as_view(),name='dashboard'),
    path('create-book/',CreateBook.as_view(),name='create_book'),
    path('delete-book/<int:book_id>/',delete_book,name='delete_book'),
    path('edit-book/<int:book_id>/',EditBook.as_view(),name='edit_book'),
    path('all-categories/',CategoriesView.as_view(),name='all_categories'),
    path('create-category/',CreateCategory.as_view(),name='create_category'),
    path('edit-category/<int:category_id>/',EditCategory.as_view(),name='edit_category'),
    path('delete-category/<int:category_id>/',delete_category,name='delete_category'),

]