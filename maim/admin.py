from django.contrib import admin

from maim.models import Cereal, NutriFact, Manufacturer

# Register your models here.

 

admin.site.register(Cereal)
admin.site.register(NutriFact)
admin.site.register(Manufacturer)
#admin.site.register(CerealSearch)


