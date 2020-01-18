from django import forms
from .models import News, Portal


class NewForm(forms.ModelForm):
    """ class created to be able to get to the database 
    by the form
    not used because it is not a system requirement
    """
    class Meta:
        model = News
        fields = ('title', 'portal')
