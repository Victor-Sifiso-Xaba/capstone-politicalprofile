# polls/forms.py
from django import forms
from .models import Choice, Question

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

ChoiceFormSet = forms.inlineformset_factory(Question, Choice, form=ChoiceForm, extra=3)  # Adjust extra as needed
