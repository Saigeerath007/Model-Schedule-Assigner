from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, ModelMultipleChoiceField, ModelChoiceField


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


PREF_CHOICES = (
    (0, "Select"),
    (1, "One"),
    (2, "Two"),
    (3, "Three"),
    (4, "Four"),
    (5, "Five"),
)


class Preferences(forms.Form):
    # pref_1 = forms.ChoiceField(choices=PREF_CHOICES, label="First Preference", initial='', widget=forms.Select(), required=True)
    # pref_2 = forms.ChoiceField(choices=PREF_CHOICES, label="Second Preference", initial='', widget=forms.Select(), required=True)
    # pref_3 = forms.ChoiceField(choices=PREF_CHOICES, label="Third Preference", initial='', widget=forms.Select(), required=True)
    # pref_4 = forms.ChoiceField(choices=PREF_CHOICES, label="Fourth Preference", initial='', widget=forms.Select(), required=True)
    # pref_5 = forms.ChoiceField(choices=PREF_CHOICES, label="Fifth Preference", initial='', widget=forms.Select(), required=True)

    pref_1 = forms.IntegerField()
    pref_2 = forms.IntegerField()
    pref_3 = forms.IntegerField()
    pref_4 = forms.IntegerField()
    pref_5 = forms.IntegerField()
