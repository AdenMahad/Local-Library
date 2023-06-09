from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name= 'authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name= 'author-detail'),
    path("accounts/login/", auth_views.LoginView.as_view(),),
    path('accounts/logout/',auth_views.LogoutView.as_view(),),
    path('register/',views.register, name='register')

    

]