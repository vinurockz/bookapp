from django import forms
from .models import Create_Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Create_Form(forms.Form):

    book_name=forms.CharField()
    author=forms.CharField()
    choices=(("Malyalam","Malayal"),("English","Englis"),("Hindi","Hind"),("Unknown_Lang","Unknown_Lang"))
    language=forms.ChoiceField(choices=choices)
    pages=forms.CharField()
    price=forms.CharField()

class Update_Form(forms.ModelForm):
    class Meta:
        model=Create_Model
        fields='__all__'

class Registration_Form(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]

class Login_Form(forms.Form):
    username=forms.CharField()
    password=forms.CharField()



