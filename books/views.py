from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from books.models import Book

# Create your views here.

def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/home.html', context)



class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
    ordering = ['-date_posted']
