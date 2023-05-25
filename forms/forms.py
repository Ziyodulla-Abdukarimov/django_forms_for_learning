from django import forms
from .models import Blog
from django.forms import modelformset_factory
from .models import Person

PersonFormSet = modelformset_factory(Person, fields=('name', 'age'), extra=1)


class InputForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(max_length=1000)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
