
from django.conf.urls import include, url
from django.contrib import admin
from books.views import*  #current_datetime,homepage,search_form

urlpatterns = [
	url(r'^$',homepage),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/$',search),
	url(r'^search/details/',details),
	url(r'^edit/',edit),
	url(r'^delete/',delete),
	url(r'^newone/',newone),
	url(r'^saveedit/',saveEdit),
	url(r'^about/',about),
]
