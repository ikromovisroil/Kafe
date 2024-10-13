from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from users.models import *


class Userprofilform(UserChangeForm):
    class Meta:
        model = User
        fields = ('name','first_name','last_name','image',)

    def __init__(self,*args,**kwargs):
        super(Userprofilform,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class Usercomment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name','title','summa','image',)
        
        
class EmployeeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('rol','username','password1','password2','first_name','last_name','tel',)


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('name',)
