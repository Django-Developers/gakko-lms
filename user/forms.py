from django import forms
from django.contrib.auth import  get_user_model 
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
class ExtendedUserCreationForm(UserCreationForm):
    # university_ID=forms.CharField(max_length=30,required=True)
    email=forms.EmailField(required=True)
    full_name=forms.CharField(max_length=155)

    class Meta:
        model=User
        fields=('username','email','full_name','password1','password2')
    def save(self, commit=True):
        user = super().save(commit=False)

        # user.university_ID=self.cleaned_data['university_ID']
        user.email=self.cleaned_data['email']
        user.full_name=self.cleaned_data['full_name']

        if commit:
            user.save()
        return user