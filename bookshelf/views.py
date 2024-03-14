from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from rest_framework import viewsets
from .forms import *
from .models import *
from .serializers import *
# Create your views here.


@login_required
def main_page(request):
    num_books = Book.objects.all().count()
    bar_num = BarCode.objects.all().count()
    user_num = Log_user.objects.all().count()
    ln_books = A_Logger.objects.filter(status__exact='On loan').count()
    #avail_books=A_Logger.objects.filter(status__exact ='On loan').count()
    av_book = num_books-ln_books
    context = {
        'book': num_books,
        'bar_code': bar_num,
        'num_users': user_num,
        'book_onloan': ln_books,
        'book_av': av_book,
        # 'num_authors': num_authors,
    }
    return render(request, 'bookshelf/index.html', context=context)


class Books(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    # your own name for the list as a template variable
    template = "bookshelf/book_list.html"
    queryset = Book.objects.all(
    )  # Get 5 books containing the title war  # Specify your own template name/location """ """


class Authors(generic.ListView):
    model = Author
    context_object_name = 'auth_list'
    template = 'bookshelf/author_list.html'
    queryset = Author.objects.all()


class Logged(generic.ListView):
    model = A_Logger
    context_object_Name = 'log_user_list'
    template = 'bookshelf/a_logger_list.html'
    queryset = A_Logger.objects.filter(status__exact='On loan')


def book_add_view(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, "bookshelf/add_book.html", context)


def barcodeadd(request):
    form = BarcodeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BarcodeForm()
    context = {
        'form': form
    }
    return render(request, "bookshelf/baradd.html", context)


def useradd(request):
    form = Log_userForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = Log_userForm()
    context = {
        'form': form
    }
    return render(request, "bookshelf/useradd.html", context)


def authoradd(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, "bookshelf/authoradd.html", context)


def logger(request):
    form = LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LogForm()
    context = {
        'form': form
    }
    return render(request, "bookshelf/logger.html", context)


class Code_API_View(viewsets.ModelViewSet):
    queryset = BarCode.objects.all()
    serializer_class = CodeSerializer


class Book_API_View(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Author_API_View(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class Log_API_View(viewsets.ModelViewSet):
    queryset = A_Logger.objects.all()
    serializer_class = LoggerSerializer


class User_API_View(viewsets.ModelViewSet):
    queryset = Log_user.objects.all()
    serializer_class = UserSerializer


class Users(generic.ListView):
    model = Log_user
    context_object_name = 'log_user_list'
    # your own name for the list as a template variable
    template = "bookshelf/log_user_list.html"
    queryset = Log_user.objects.all()


class BookSearch(generic.ListView):
    model = Book

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__full_name__icontains=query) | Q(
                MRP__icontains=query) | Q(category__icontains=query)
        )
        return object_list


class logSearch(generic.ListView):
    model = Log_user

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Log_user.objects.filter(
            Q(Name__icontains=query)
        )
        return object_list


@login_required
def Dellog(request):
    form = logdelform(request.POST or None)
    #logs=A_Logger.objects.filter(status__exact='On loan')
    if form.is_valid():
        logs = A_Logger.objects.all()
        code = request.POST.get('bar_code_no')
        item = A_Logger.objects.filter(bar_code_no__exact=code)
        item.delete()
        form = logdelform()
    context = {
        'form': form
    }
    return render(request, 'bookshelf/delog.html', context)
