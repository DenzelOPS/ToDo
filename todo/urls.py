from django.conf.urls import url
from todoapp.views import todolist
 
urlpatterns = [
	url(r'$^', todolist )
]