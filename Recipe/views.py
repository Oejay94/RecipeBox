from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from Recipe.models import Recipe, Author
from Recipe.forms import AddAuthor, LoginForm, SignupForm, AddRecipe


def main(request):
    main = Recipe.objects.all()
    return render(request, 'main.html', {'recipe_list': main})


def recipe(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {'data': data})


def author(request, id):
    auth = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=auth)
    return render(request, 'author.html', {'auth': auth, 'recipe': recipe})


@login_required()
def add_recipe(request):
    html = "recipe_forms.html"

    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse("main"))
    else:
        form = AddRecipe(request.user)

    return render(request, html, {'form': form})


@login_required
def add_author(request):
    html = "author_forms.html"

    if request.method == "POST":
        form = AddAuthor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse("main"))
    else:
        form = AddAuthor()

    return render(request, html, {'form': form})


def signup_view(request):
    html = 'signup_form.html'

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))

    else:
        if request.method == "POST":
            form = SignupForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(
                    data['username'], data['email'], data['password1'])
                login(request, user)
                Author.objects.create(
                    name=data['username'],
                    user=user
                )
            return HttpResponseRedirect(reverse('main'))
        else:
            form = SignupForm()

        return render(request, html, {'form': form})


def login_view(request):
    html = 'login_form.html'

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/'))
