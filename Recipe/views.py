from django.shortcuts import render, reverse, HttpResponseRedirect
from Recipe.models import Recipe, Author
from Recipe.forms import AddRecipe, AddAuthor


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

    form = AddRecipe()

    return render(request, html, {'form': form})


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
    form = AddAuthor()

    return render(request, html, {'form': form})
