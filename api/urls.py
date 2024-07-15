from django.urls import path
from .views import hello, recipe_idea, ingredient_info

urlpatterns = [
    path('hello/', hello),
    path('recipe/', recipe_idea),
    path('ingredients/', ingredient_info, name='ingredient-info'),
]