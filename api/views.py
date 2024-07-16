# import requests
import json
import os
from urllib.parse import unquote
from django.http import HttpResponse, JsonResponse
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECIPES_FILE_PATH = os.path.join(BASE_DIR, 'recipes.json')
INGREDIENTS_FILE_PATH = os.path.join(BASE_DIR, 'ingredients.json')

# Create your views here.
def hello(request):
  return HttpResponse('Hello API')

def load_recipe(recipe='chicken'):
  with open(RECIPES_FILE_PATH, 'r') as recipes_file:
    recipes_data = json.load(recipes_file)
  return recipes_data[recipe]

def load_ingredient(ingredient):
  with open(INGREDIENTS_FILE_PATH, 'r') as ingredients_file:
    ingredients_data = json.load(ingredients_file)
  return ingredients_data[ingredient]

def recipe_idea(request):
  # query = request.GET.get('q', 'chicken')
  # url = 'https://api.edamam.com/search'
  # params = {
  #   'q': query,
  #   'app_id': settings.EDAMAM_RECIPE_API_ID,
  #   'app_key': settings.EDAMAM_RECIPE_API_KEY
  # }
  # try:
  #   response = requests.get(url, params=params)
  #   response.raise_for_status()
  #   data = response.json()
  # except requests.RequestException as e:
  #   return JsonResponse({'error': str(e)}, status=500)

  # recipes = data.get('hits')

  # if not recipes:
  #   return JsonResponse({'message': 'No recipes found'}, status=404)

  # recipe = recipes[0]

  # label = recipe['recipe'].get('label')
  # image = recipe['recipe'].get('image')
  # ingredients = [ing['food'] for ing in recipe['recipe'].get('ingredients', [])]

  # filtered_data = {
  #   'label': label,
  #   'image': image,
  #   'ingredients': ingredients
  # }

  # return JsonResponse(filtered_data)

  data = load_recipe('chicken')
  return JsonResponse(data)

def ingredient_info(request):
  query = request.GET.get('ingredient', 'chicken')
  # url = 'https://api.edamam.com/api/nutrition-data'
  # params = {
  #   'ingr': ingredient,
  #   'app_id': settings.EDAMAM_NUTRITION_API_ID,
  #   'app_key': settings.EDAMAM_NUTRITION_API_KEY
  # }
  # try:
  #   response = requests.get(url, params=params)
  #   response.raise_for_status()
  #   data = response.json()
  # except requests.RequestException as e:
  #   return JsonResponse({'error': str(e)}, status=500)

  # calories = data.get('calories')
  # health_labels = data.get('healthLabels')
  
  # filtered_data = {
  #   'calories': calories,
  #   'healthLabels': health_labels
  # }

  # return JsonResponse(filtered_data)
  ingredient = unquote(query)
  data = load_ingredient(ingredient)
  return JsonResponse(data)
