from django import forms

from .models import News, Portal

class NewForm(forms.ModelForm):
  
  class Meta:
    model = News
    fields = ('title', 'portal')