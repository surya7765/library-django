from django.urls import path, include
from books.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name="book-home"),
]
