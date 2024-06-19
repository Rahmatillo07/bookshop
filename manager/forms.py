from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,min_length=4,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'type':'password'
    }))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
            }),

            'phone_number':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'phone'
            }),

            'password':forms.PasswordInput(attrs={
                'class':'form-control',

            }),
        }



        def clean_confirm_password(self):
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('confirm_password')

            if password and password2 and password != password2:
                raise forms.ValidationError('Parollar mos kelmadi')

            return password2






class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone_number','image','address']


        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),

            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
            }),

            'address': forms.TextInput(attrs={
                'class':'form-control'
            })

        }

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_role']

        widgets = {
            'user_role':forms.Select(attrs={
                'class':'form-control'
            })
        }
