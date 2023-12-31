from django.urls import path

from .views import BookListView, BookDetailView , BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('detail_book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create_book/', BookCreateView.as_view(), name='book_create'),
    path('update_book/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('delete_book/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

]