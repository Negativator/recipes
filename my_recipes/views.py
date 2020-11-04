from django.shortcuts import render, redirect

# Create your views here.
from my_recipes.models import Recipe
from my_recipes.forms import RecipeForm


def index(req):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(req, 'index.html', context)


def create(req):
    if req.method == 'GET':
        context = {
            'form': RecipeForm(),
        }
        return render(req, 'create.html', context)
    else:
        form = RecipeForm(req.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('index')
        context = {
            'form': RecipeForm(),
        }
        return render(req, 'create.html', context)


def edit(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(instance=recipe)
    context = {
        'recipe': recipe,
        'form': form,
    }
    if req.method == 'GET':
        return render(req, 'edit.html', context)
    else:
        form = RecipeForm(req.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
            'recipe': recipe
        }
        return render(req, 'edit.html', context)


def delete(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe,
    }
    if req.method == 'GET':
        return render(req, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def details(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(', ')
    }
    return render(req, 'details.html', context)
