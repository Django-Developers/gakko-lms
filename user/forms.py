from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user.models import User


class ExtendedUserCreationForm(UserCreationForm):
    # university_ID=forms.CharField(max_length=30,required=True)
    # email=forms.EmailField(required=True)
    # full_name=forms.CharField(max_length=155)

    class Meta:
        model=User
        fields=('username','email','password1','password2')
    # def save(self, commit=True):
    #     user = super().save(commit=False)

    #     user.university_ID=self.cleaned_data['university_ID']
    #     user.email=self.cleaned_data['email']
    #     user.full_name=self.cleaned_data['full_name']

    #     if commit:
    #         user.save()
    #     return user


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password')

    # class Meta:
    #     model = User
    #     fields=('username','email','password')

    # def clean(self):
    #     email= self.cleaned_data['email']
    #     password = self.cleaned_data['password']
    #     if not authenticate(email=email,password=password):
    #         raise forms.ValidationError("Invalid login")
