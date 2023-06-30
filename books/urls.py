from django.urls import path

from .views import BookListView, BookDetailView , BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('detail_book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create_book/', BookCreateView.as_view(), name='book_create')
]