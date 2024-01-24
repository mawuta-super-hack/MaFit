from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'weight_now', 'weight_purpose', 'photo')
        labels = {
            'weight_now': 'Текущий вес',
            'weight_purpose': 'Желаемый вес',
            'photo': 'Фото',
        }


class UserWeightForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('weight_now', 'weight_purpose', 'photo')

