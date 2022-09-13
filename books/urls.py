from django.urls import path, include
from books.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name="book-home"),
    # path('user/<str:id>/', UserPostListView.as_view(), name="user-posts"),
    # path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    # path('about/', views.about, name='blog-about'),
]
