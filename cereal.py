#!/usr/bin/env python
import csv
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro.settings")

import django
django.setup()

from maim.models import Cereal, NutriFact, Manufacturer 

print os.path.abspath(__file__)

print os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cereal.csv")

 # csv_file_path2 = "%s/cereal.csv" % os.path.dirname(os.path.abspath(__file__))




csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)


for row in reader:
 
	print row 
	manufacturer_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])
	manufacturer_obj.name = row['Manufacturer']
	manufacturer_obj.save()

	name=row['Cereal Name']
	if name: 
		cereal_obj, created = Cereal.objects.get_or_create(name=row['Cereal Name'])
		cereal_obj.name = row['Cereal Name']
		cereal_obj.cups_per_serving = row['Cups per Serving']
		cereal_obj.serving_size_weight = row['Serving Size Weight']
		cereal_obj.display_shelf = row ['Display Shelf']
		cereal_obj.t_ype = row['Type']
		cereal_obj.manufacturer = manufacturer_obj
		cereal_obj.save()



		nutri_obj, created = NutriFact.objects.get_or_create(Cereal=cereal_obj)
		nutri_obj.calories = row ['Calories']
		nutri_obj.protein = row['Protein (g)']
		nutri_obj.fat = row['Fat']
		nutri_obj.sodium = row['Sodium']
		nutri_obj.dietary_fiber = row['Dietary Fiber']
		nutri_obj.carbs = row['Carbs']
		nutri_obj.sugars = row['Sugars']
		nutri_obj.potassium = row['Potassium']
		nutri_obj.vitamins = row['Vitamins and Minerals']
		nutri_obj.save()

	


