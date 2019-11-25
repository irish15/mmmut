from django import forms
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.contrib.auth import get_user_model

User = get_user_model()

class MyForm(forms.Form):
    text = forms.CharField(
        label='Image Name ',
        max_length=100,
        required=True,
        widget=forms.TextInput()
    )

class PhotoForm(forms.Form):
    image = forms.ImageField()


class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる


class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = User
       fields = ("username", "password1", "password2",)

    # class Meta:
    #     model = User
    #     fields = ('email',)
    # 
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'
    # 
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     User.objects.filter(email=email, is_active=False).delete()
    #     return email

                    