from django import forms
import project.settings as settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# TODO создайте здесь все необходимые формы


class TemplateForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))