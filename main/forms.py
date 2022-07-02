from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# class SettingsForm(forms.ModelForm):
#     q1 = forms.BooleanField()
#
#     def __init__(self):
#         if check_something():
#             self.fields['q1'].initial = True
#     class Meta:
#         model = Pro


class QuestionareForm(forms.ModelForm):
    class Meta:
        model = Questionaire
        fields = '__all__'
