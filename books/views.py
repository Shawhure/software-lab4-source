from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
import datetime
from models import Book,Author
	
def homepage(request):
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def search(request):
	error = False
	if 'auth' in request.GET:
		auth = request.GET['auth']
		if not auth:
			error = True
		else:
			books = Book.objects.filter(AuthorID__Name__icontains=auth)
			return render_to_response('search_result.html',{'query':auth,'books':books})
	return render_to_response('search_form.html', {'error': error})
def details(request):
	isbn = request.GET["isbn"]
	books = Book.objects.filter(ISBN__icontains=isbn)
	return render_to_response('details.html',{'book':books[0]})
	
def delete(request):
	isbn = request.GET.get("isbn")
	books = Book.objects.filter(ISBN__icontains=isbn)
	title = books[0].Title
	books.delete()
	return render_to_response('delete.html',{'title':title})

def edit(request):
	if 'isbn' in request.GET:
		isbn = request.GET["isbn"]
		books = Book.objects.filter(ISBN=isbn)
		book = books[0]
		return render_to_response('edit.html', {
												'error': False,
												'authorID':book.AuthorID.AuthorID,
												'title':book.Title,
												'name':book.AuthorID.Name,
												'age':book.AuthorID.Age,
												'country':book.AuthorID.Country,
												'isbn':book.ISBN,
												'price':book.Price,
												'pub':book.Publisher,
												'pubdate':book.PublishDate,
												'success':False,
												}
								)
	else:
		return render_to_response('404.html')
	
def saveEdit(request):
		error = False
		if 'title' and 'authorID' and 'name' and 'age' and 'country' and 'ISBN' and 'price' and 'pub' and 'pubdate' in request.GET:
			authorID = request.GET['authorID']
			title = request.GET['title']
			name = request.GET['name']
			age = request.GET['age']
			country = request.GET['country']
			isbn = request.GET['ISBN']
			price = request.GET['price']
			pub = request.GET['pub']
			pubdate = request.GET['pubdate']
			if (not title) or (not name) or (not age) or (not country) or (not isbn) or (not price) or (not pub) or (not pubdate):
				error = True
				return render_to_response('edit.html', {
														'error': error,
														'authorID':authorID,
														'title':title,
														'name':name,
														'age':age,
														'country':country,
														'isbn':isbn,
														'price':price,
														'pub':pub,
														'pubdate':pubdate,
														'success':False,
														}
										)
			else:
				author = Author.objects.filter(AuthorID = authorID)
				author.update(AuthorID = authorID,Name = name,Age = age,Country = country)
				Book.objects.filter(ISBN = isbn).update(ISBN = isbn,Title = title,Price = price,Publisher = pub,PublishDate = pubdate)
				return render_to_response('edit.html', {
														'error': error,
														'authorID':authorID,
														'title':title,
														'name':name,
														'age':age,
														'country':country,
														'isbn':isbn,
														'price':price,
														'pub':pub,
														'pubdate':pubdate,
														'success':True,
														}
										)
		else:
			return render_to_response('404.html')
def newone(request):
	error = False
	if 'title' in request.GET and 'authorID' in request.GET and 'name' in request.GET and 'age' in request.GET \
		and 'country' in request.GET and 'isbn' in request.GET and 'price' in request.GET \
		and 'pub' in request.GET and 'date' in request.GET:
		authorID = request.GET['authorID']
		title = request.GET['title']
		name = request.GET['name']
		age = request.GET['age']
		country = request.GET['country']
		isbn = request.GET['isbn']
		price = request.GET['price']
		pub = request.GET['pub']
		date = request.GET['date']
		if (not title) or (not name) or (not age) or (not country) or (not isbn) or (not price) or (not pub) or (not date):
			error = True
		else:
			author = Author(AuthorID = authorID,Name = name,Age = age,Country = country)
			
			books = Book(ISBN = isbn,Title = title,AuthorID = author,Price = price,Publisher = pub,PublishDate = date)
			author.save()
			books.save()
	return render_to_response('newone.html', {'error': error})

def about(request):
	return render_to_response('about.html')

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
