from django.forms import ModelForm
from django.forms.widgets import *
from Users.models import Profile



class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }
        exclude = ['first_name', 'last_name', 'groups', 'user_permissions', 'last_login', 'date_joined', 'partner_points']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.is_active = True
            user.save()
        return user
