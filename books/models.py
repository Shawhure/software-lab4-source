from django.db import models
from django.contrib import admin

class Author(models.Model):
    AuthorID = models.CharField(max_length=40,primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Country = models.CharField(max_length=20)

class Book(models.Model):
	ISBN = models.CharField(max_length=40,primary_key=True)
	Title = models.CharField(max_length=100)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length=40)
	PublishDate = models.DateField()
	Price = models.FloatField()
	
	
'''Classes of manage backend database for django administration'''

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('Name','Age','Country')

class BookAdmin(admin.ModelAdmin):
	list_display = ('Title','Publisher','Price')
	
    
