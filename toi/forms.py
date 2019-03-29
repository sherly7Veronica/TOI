from django import forms
from .models import Level1, Level2, Level3


class Level1Form(forms.ModelForm):

	class Meta:
		model = Level1
		fields = ('name',)


# class Level2Form(forms.ModelForm):
#
# 	class Meta:
# 		model = Level2
# 		fields = ()
#
#
# class Level3Form(forms.ModelForm):
#
# 	class Meta:
# 		model = Level3
# 		fields = ()