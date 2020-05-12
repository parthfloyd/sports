from django.contrib import admin
from .models import Match

#Customize your models here.
class MatchAdmin(admin.ModelAdmin):
	fieldsets=[
		("Date & Time",{"fields": ["date", "time"]}),
		("Match Specific Details",{"fields":["sport", "location","maxPlayers"]})
	]

# Register your models here.
admin.site.register(Match, MatchAdmin)