from django.urls import reverse_lazy
from django.views import generic

from .models import BOOK

# Create your views here.

class BookListView(generic.ListView):
    model = BOOK
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = BOOK
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = BOOK
    fields = ['title', 'author', 'content', 'price']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = BOOK
    fields = ['title', 'author', 'content', 'price']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = BOOK
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')