from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Books', views.Book_API_View)
router.register('BarCode', views.Code_API_View)
router.register('Authors', views.Author_API_View)
router.register('Logs', views.Log_API_View)
router.register('Users', views.User_API_View)
urlpatterns = [
    path('', views.main_page, name='index'),
    path('books/', views.Books.as_view(), name='books'),
    path('authors/', views.Authors.as_view(), name='authors'),
    path('users/', views.Users.as_view(), name='users'),
    path('logs/', views.Logged.as_view(), name='logs'),
    path('bookadd/', views.book_add_view, name='bookadd'),
    path('barcodeadd/', views.barcodeadd, name='barcodeadd'),
    path('authoradd/', views.authoradd, name='authoradd'),
    path('useradd/', views.useradd, name='useradd'),
    path('log/', views.logger, name='logger'),
    path('delog/', views.Dellog, name='delog'),
    #path('bsearch/', views.bsearch.as_view(),name="booksearch"),
    #path('usearch/', views.usearch.as_view(),name="usersearch"),
    path('booksearches/', views.BookSearch.as_view(), name="bsearch"),
    path('usersearches/', views.logSearch.as_view(), name="usearch"),
    path('API/', include(router.urls)),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
