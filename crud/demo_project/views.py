from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Demo_project_Db


class CreateView(CreateView):  # Creates the view to insert text to database
    model = Demo_project_Db
    fields = [
        "title", "description"
    ]
    template_name = 'home.html'
    success_url = 'list'


class ListTheView(ListView):  # list the texts inserted into the database into the html file created here
    model = Demo_project_Db
    template_name = 'listView.html'


# Create your views here.


class UpdateTheView(UpdateView):  # list the texts inserted into the database into the html file created here
    model = Demo_project_Db
    fields = [
        "title", "description"
    ]
    template_name = 'Update.html'
    success_url = '/'

class DeleteTheView(DeleteView):
    model = Demo_project_Db
    template_name = 'Delete.html'
    success_url = '/'