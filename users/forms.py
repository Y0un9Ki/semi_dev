from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(min_length=3,
                               widget=forms.TextInput(
                                   attrs={'placeholder': '사용자명(3자리 이상)'},
                               ),
                               )
    password = forms.CharField(min_length=4,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder':'비밀번호(4자리 이상)'},
                               ),
                               )
    
class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    location = forms.CharField()