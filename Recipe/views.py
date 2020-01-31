from django.shortcuts import render
from Recipe.models import Recipe, Author


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
