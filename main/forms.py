from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Subject, GuestCustomer, City


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')


class GuestCustomerForm(forms.ModelForm):
    subject = forms.ModelChoiceField(empty_label='Chọn môn học', queryset=Subject.objects.all())
    city_name = forms.ModelChoiceField(empty_label='Chọn thành phố', queryset=City.objects.all())

    class Meta:
        model = GuestCustomer
        fields = ['subject', 'city_name', 'level', 'budget', 'guest_name', 'email', 'phone_number']
