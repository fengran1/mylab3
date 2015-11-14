#coding=utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import Author,Book
#from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.method == 'GET':
        if 'delete' in request.GET and request.GET['delete']:
            fordelete = request.GET['delete']
            bookdelete = Book.objects.filter(ISBN = fordelete)
            bookdelete.delete()
    books = Book.objects.all()
    return render_to_response('index.html',{'booknames':books})
def search(request):
    if request.method == 'GET':
        if 'search' in request.GET and request.GET['search']:
            forsearch = request.GET['search']
            if Author.objects.filter(Name = forsearch):
                authorsearch = Author.objects.get(Name = forsearch)
                #booksearch = authorsearch.books.all()
                booksearch = Book.objects.filter(AuthorID = authorsearch.AuthorID)
                return render_to_response('search.html',{'author':authorsearch,'booknames':booksearch})
            else:
                error = "The Author's name you have input is not exist!"
                return render_to_response('search.html',{'error':error})
        else:
            error = "Please input an author name!"
            return render_to_response('search.html',{'error':error})
    return render_to_response('search.html')
def bookinformation(request,i):
    ISBN = i
    if Book.objects.filter(ISBN = ISBN):
        book = Book.objects.get(ISBN = ISBN)
        author = Author.objects.get(AuthorID = book.AuthorID.AuthorID)
        return render_to_response('information.html',{'author':author,'book':book})
    else:
        error = "This book is not exist!"
        return render_to_response('information.html',{'error':error})
        
@csrf_exempt   
def update(request,i):
    ISBN = i
    if Book.objects.filter(ISBN = ISBN):
        book = Book.objects.get(ISBN = ISBN)
        author = Author.objects.all()
        if request.method == 'POST':
            book.Title = request.POST['Title']
            book.Publisher = request.POST['Publisher']
            book.PublishDate = request.POST['PublishDate']
            book.Price = request.POST['Price']
            ID = request.POST.get('select')
            book.AuthorID = Author.objects.get(AuthorID = ID)
            book.save()
        return render_to_response('update.html',{'options':author,'book':book})
    else:
        error = "This book is not exist!"
        return render_to_response('update.html',{'error':error})
        
@csrf_exempt        
def addbook(request):
    author = Author.objects.all()
    if request.method == 'POST':
        if not Book.objects.filter(ISBN = request.POST['ISBN']):
            ID = request.POST.get('select')
            Book.objects.create(ISBN = request.POST['ISBN'], Title = request.POST['Title'], AuthorID = Author.objects.get(AuthorID = ID),Publisher = request.POST['Publisher'], PublishDate = request.POST['PublishDate'], Price = request.POST['Price'])
            return render_to_response('addbook.html',{'options':author})
        else:
            error = "The book ISBN is already exist,or your input is awful!"
            return render_to_response('addbook.html',{'options':author, 'error':error})
    return render_to_response('addbook.html',{'options':author})
    
@csrf_exempt 
def addauthor(request):
    if request.method == 'POST':
        if not Author.objects.filter(AuthorID = request.POST['AuthorID']):
            Author.objects.create(AuthorID = request.POST['AuthorID'], Name = request.POST['Name'], Age = request.POST['Age'], Country = request.POST['Country'])
            return render_to_response('addauthor.html')
        else:
            error = "The AuthorID is already exist,or your input is awful!"
            return render_to_response('addauthor.html',{'error':error})
    return render_to_response('addauthor.html')
            