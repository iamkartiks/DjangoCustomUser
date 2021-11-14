from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email','address','username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','address','username')

class EmailEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class UsernameEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username',)

class AddressEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('address',)