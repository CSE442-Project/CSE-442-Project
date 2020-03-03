from django import forms
from . import models
from django.contrib.auth.models import User


class ContractorCreationForm(forms.Form):
    username = forms.CharField(label='Enter username', max_length=50)
    first_name = forms.CharField(label='Enter first name', max_length=50)
    last_name = forms.CharField(label='Enter last name', max_length=50)
    email = forms.EmailField(label='Enter email')
    phone = forms.IntegerField()
    password_1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError(
                'The password fields do not match.',
                code='password_mismatch'
            )
        return password_2

    def _create_auth_user(self):
        user = User(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password_1'],
        )
        user.save()
        return user

    def create_contractor(self):
        user = self._create_auth_user()
        profile = models.ContractorProfile(
            user=user,
            phone=self.cleaned_data['phone'],
        )
        profile.save()

    def __init__(self, *args, **kwargs):
        super(ContractorCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-field'
