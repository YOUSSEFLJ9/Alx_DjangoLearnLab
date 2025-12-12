from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .viewz.admin_view import admin_view
from .viewz.librarian_view import librarian_view
from .viewz.member_view import member_view



urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('register/', views.register, name='register'),
    path("admin-dashboard/", admin_view, name="admin_view"),
    path("librarian-dashboard/", librarian_view, name="librarian_view"),
    path("member-dashboard/", member_view, name="member_view"),
]