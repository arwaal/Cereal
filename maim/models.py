from django.db import models

# Create your models here.


class Cereal(models.Model):
	name = models.CharField(max_length=50, unique=True, null=True)
	serving_size_weight = models.FloatField(null=True)
	cups_per_serving = models.FloatField(null=True)
	display_shelf = models.FloatField(null=True)
	t_ype = models.CharField(max_length=2,null=True)
	manufacturer = models.ForeignKey('maim.Manufacturer', null=True)
	image = models.ImageField(upload_to="cereal", null=True)
	info = models.TextField()

	def __unicode__(self):
		return self.name

	

class NutriFact(models.Model):
	#name = models.CharField(max_length=50)
	calories = models.IntegerField(null=True)
	protein = models.FloatField(null=True)
	fat = models.FloatField(null=True)
	sodium = models.FloatField(null=True)
	dietary_fiber = models.FloatField(null=True)
	carbs = models.FloatField(null=True)
	sugars = models.FloatField(null=True)
	potassium = models.FloatField(null=True)
	vitamins = models.FloatField(null=True)
	Cereal = models.OneToOneField('maim.Cereal', null=True)
	def __unicode__(self):
		return self.Cereal.name
		
	def nutri(self):
		nutri_list=[]
		nutri_list.append("Protein: %s" % self.protein)
		nutri_list.append("Calories: %s " % self.calories)
		nutri_list.append("Fat: %s " % self.fat)
		nutri_list.append("Sodium: %s " % self.sodium)
		nutri_list.append("Dietary Fiber: %s" % self.dietary_fiber)
		nutri_list.append("Carbs: %s " % self.carbs)
		nutri_list.append("Sugars: %s" % self.sugars)
		nutri_list.append("Potassium: %s" % self.potassium)

		return nutri_list

class Manufacturer(models.Model):
	name = models.CharField(max_length=50, null=True)
	def __unicode__(self):
		return self.name








