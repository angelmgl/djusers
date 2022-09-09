from django import forms

from .models import User


class UserRegisterForm(forms.ModelForm):

    custom_password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Introduzca su contraseña'
            }
        )
    )

    repeat_password = forms.CharField(
        label="Repetir contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repita su contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'full_name',
            'email',
            'username',
            'gender',
            'age'
        )

    def clean_repeat_password(self):
        if self.cleaned_data['custom_password'] != self.cleaned_data['repeat_password']:
            self.add_error('repeat_password', 'Las contraseñas no coinciden')
