from maim.models import Manufacturer

def main_menu(request):

	manu = Manufacturer.objects.all()

	return {'main_menu': manu }