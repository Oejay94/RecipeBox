from django import forms
from Recipe.models import Author


class AddRecipe(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.Textarea()
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
