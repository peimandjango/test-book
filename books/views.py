
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