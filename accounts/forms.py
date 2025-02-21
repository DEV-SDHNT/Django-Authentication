from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirmPassword=cleaned_data.get('confirmPassword')
        if password!=confirmPassword and password and confirmPassword:
            self.add_error('confirmPassword',"Passwords do not match")
        return cleaned_data