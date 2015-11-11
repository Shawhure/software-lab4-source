#coding:utf-8

import sae  
  
from pickbooksup import wsgi
  
application = sae.create_wsgi_app(wsgi.application)  

#fix a bug 
#bug's id=2