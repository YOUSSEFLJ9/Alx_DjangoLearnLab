from django.urls import include, path
from . import views
from django.contrib.auth import login
# from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
# from django.contrib.auth.views import LogoutView


#how to use login and logout views


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', views.register, name='register'),
]