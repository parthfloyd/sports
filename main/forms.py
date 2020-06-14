from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Match
from django.forms import DateField
import html5.forms.widgets as html5_widgets


"""--------- Forms ----------- """
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		if (commit):
			user.save()
		return user

class NewUserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('age','city')

class NewMatchForm(forms.ModelForm):
	class Meta:
		model = Match
		fields = ('location','sport','maxPlayers','date','time')
		widgets = {
            'date': html5_widgets.DateInput,
            'time': html5_widgets.TimeInput
        }
		