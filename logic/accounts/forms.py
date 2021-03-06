from django import forms
from . import models
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from logic.settings import EMAIL_HOST_USER


class ClientCreationForm(forms.Form):
    username = forms.CharField(label='Enter username', max_length=50)
    first_name = forms.CharField(label='Enter first name', max_length=50)
    last_name = forms.CharField(label='Enter last name', max_length=50)
    email = forms.EmailField(label='Enter email')
    phone = forms.IntegerField()
    password_1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    street_1 = forms.CharField(label='Enter first street address', max_length=100)
    street_2 = forms.CharField(
        label='Enter second street address',
        max_length=100,
        required=False
    )
    street_3 = forms.CharField(
        label='Enter third street address',
        max_length=100,
        required=False
    )
    city = forms.CharField(label='Enter city', max_length=100)
    state = forms.CharField(label='Enter state', max_length=50)
    zip = forms.IntegerField(label='Enter zip code')
    dw_size = forms.IntegerField(
        label='Enter the number of cars your driveway can hold'
    )

    def clean_username(self):
        existing = User.objects.filter(username=self.cleaned_data['username']).all()
        if len(existing) != 0:
            raise forms.ValidationError(
                'An account with this username already exists.',
                code='existing_username'
            )
        return self.cleaned_data['username']

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
        )
        user.set_password(self.cleaned_data['password_1']);
        user.save()
        client_group = Group.objects.get_or_create(name='client')[0]
        user.groups.add(client_group)
        fname = user.first_name
        lname = user.last_name
        subject = 'Your PlowMe Account Has Been Created'
        message = ('Hi ' + str(fname) + ' ' + str(lname) + ', Your PlowMe client account has just been created successfully. If this was not you, please respond to this email so we can deactivate the account.')
        recipient = user.email
        send_mail(subject, message, EMAIL_HOST_USER, [recipient])
        return user

    def _create_address(self):
        address = models.Address(
            street_1=self.cleaned_data['street_1'],
            street_2=self.cleaned_data['street_2'],
            street_3=self.cleaned_data['street_3'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            zip=self.cleaned_data['zip']
        )
        address.save()
        return address

    def create_client(self):
        user = self._create_auth_user()
        address = self._create_address()
        profile = models.ClientProfile(
            user=user,
            address=address,
            phone=self.cleaned_data['phone'],
            dw_size=self.cleaned_data['dw_size']
        )
        profile.save()

    def __init__(self, *args, **kwargs):
        super(ClientCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-field'


class ContractorCreationForm(forms.Form):
    username = forms.CharField(label='Enter username', max_length=50)
    first_name = forms.CharField(label='Enter first name', max_length=50)
    last_name = forms.CharField(label='Enter last name', max_length=50)
    email = forms.EmailField(label='Enter email')
    phone = forms.IntegerField()
    password_1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        existing = User.objects.filter(username=self.cleaned_data['username']).all()
        if len(existing) != 0:
            raise forms.ValidationError(
                'An account with this username already exists.',
                code='existing_username'
            )
        return self.cleaned_data['username']

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
        )
        user.set_password(self.cleaned_data['password_1']);
        user.save()
        contractor_group = Group.objects.get_or_create(name='contractor')[0]
        user.groups.add(contractor_group)
        fname = user.first_name
        lname = user.last_name
        subject = 'Your PlowMe Account Has Been Created'
        message = ('Hi ' + str(fname) + ' ' + str(lname) + ', Your PlowMe contractor account has just been created successfully. If this was not you, please respond to this email so we can deactivate the account.')
        recipient = user.email
        send_mail(subject, message, EMAIL_HOST_USER, [recipient])
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
