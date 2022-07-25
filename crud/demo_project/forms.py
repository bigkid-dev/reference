from django import forms
from .models import Demo_project_Db, UserModel


class CrudForms(forms):
    class Meta:
        model = Demo_project_Db
        fields = ["title", "description"]


class UserForm(UserModel):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]