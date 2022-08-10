from django import forms
from .models import *





# class SettingsForm(forms.ModelForm):
#     q1 = forms.BooleanField()
#
#     def __init__(self):
#         if check_something():
#             self.fields['q1'].initial = True
#     class Meta:
#         model = Pro

from snowpenguin.django.recaptcha3.fields import ReCaptchaField
class QuestionareForm(forms.ModelForm):
    # captcha = ReCaptchaField()
    class Meta:
        model = Questionaire
        fields = '__all__'

class ShortQuestionaireForm(forms.ModelForm):
    # captcha = ReCaptchaField()
    class Meta:
        model = ShortQuestionaire
        fields = ['company_contact_phone', 'email', 'fio', 'inn']

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # captcha = ReCaptchaField()
