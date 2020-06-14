from django.contrib import admin
from .models import Match, UserProfile

#Inline models to handle ManyToManyRelationship
class playerInline(admin.TabularInline):
	model = UserProfile.matches.through
#Customize your models here.
class MatchAdmin(admin.ModelAdmin):
	fieldsets=[
		("Date & Time",{"fields": ["date", "time"]}),
		("Match Specific Details",{"fields":["sport", "location","maxPlayers"]})
	]

	inlines = [playerInline]

# Register your models here.
admin.site.register(Match, MatchAdmin)
admin.site.register(UserProfile)