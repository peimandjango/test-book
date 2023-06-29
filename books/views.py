
from django.views import generic

from .models import BOOK
# Create your views here.

class BookListView(generic.ListView):
    model = BOOK
    template_name = 'books/book_list'
    context_object_name = 'books'