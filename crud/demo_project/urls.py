from django.urls import path
from .views import CreateView, ListTheView, UpdateTheView, DeleteTheView

# path is a variable imported from django.urls to route your views.py to the respective html file
# without this code the backend wont tell the browser which html page to navigate to

urlpatterns = [
    path("", CreateView.as_view(), name="Home"),
    path("list/", ListTheView.as_view()),
    path("<pk>/update", UpdateTheView.as_view()),
    path("<pk>/delete", DeleteTheView.as_view())
]