import requests
from django.http import HttpResponse, JsonResponse
from django.conf import settings

# Create your views here.
def hello(request):
  return HttpResponse('Hello API')

def recipe_idea(request):
  query = request.GET.get('q', 'chicken')
  url = 'https://api.edamam.com/search'
  params = {
    'q': query,
    'app_id': settings.EDAMAM_RECIPE_API_ID,
    'app_key': settings.EDAMAM_RECIPE_API_KEY
  }
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
  except requests.RequestException as e:
    return JsonResponse({'error': str(e)}, status=500)

  recipes = data.get('hits')

  if not recipes:
    return JsonResponse({'message': 'No recipes found'}, status=404)

  recipe = recipes[0]

  label = recipe['recipe'].get('label')
  image = recipe['recipe'].get('image')
  ingredients = [ing['food'] for ing in recipe['recipe'].get('ingredients', [])]

  filtered_data = {
    'label': label,
    'image': image,
    'ingredients': ingredients
  }

  return JsonResponse(filtered_data)

def ingredient_info(request):
  ingredient = request.GET.get('ingredient', 'apple')
  url = 'https://api.edamam.com/api/nutrition-data'
  params = {
    'ingr': ingredient,
    'app_id': settings.EDAMAM_NUTRITION_API_ID,
    'app_key': settings.EDAMAM_NUTRITION_API_KEY
  }
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
  except requests.RequestException as e:
    return JsonResponse({'error': str(e)}, status=500)

  calories = data.get('calories')
  health_labels = data.get('healthLabels')
  
  filtered_data = {
    'calories': calories,
    'healthLabels': health_labels
  }

  return JsonResponse(filtered_data)
