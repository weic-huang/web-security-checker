from django.urls import path
from WebApp.views import Frontend

front=Frontend()

urlpatterns = [
	 path('', front.index, name='index'),
]