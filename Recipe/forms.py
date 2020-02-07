from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Recipe.models import Author


class AddRecipe(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(AddRecipe, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['author'].queryset = Author.objects.filter(user=user)


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.'
    )
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.'
    )
    email = forms.EmailField(
        max_length=250, help_text='Required, enter a valid email address.'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
