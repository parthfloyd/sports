import django_filters
from .models import *

class MatchFilter(django_filters.FilterSet):
	class Meta:
		model = Match
		fields = {'id': ['exact'],
				  'sport': ['icontains'],
				  'location':['icontains']}