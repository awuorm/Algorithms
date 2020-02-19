#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  quantities = []
  if len(recipe) == len(ingredients):
    while len(quantities) != len(ingredients):
      for key in ingredients:
        batches = ingredients[key]/recipe[key]
        if batches < 1:
          quantities.append(0)
        else:
          batches = ingredients[key]//recipe[key]
          quantities.append(batches)
      print(quantities)
      if 0 in quantities:
        print(0)
        return 0
      else:
        print(min(quantities))
        return min(quantities)
  else:
      return 0
  
      
          
          
          
        
      


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))