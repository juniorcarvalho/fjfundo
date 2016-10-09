from django import forms
from django.contrib.auth import authenticate
from fjfundo.core.models import MyUser


class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, required=True)

    class Meta:
        model = MyUser
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            if not user.is_active:
                raise forms.ValidationError("Conta não está ativa.")
        else:
            raise forms.ValidationError("Email / senha não são válidos.")
        return self.cleaned_data


class EditAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = MyUser.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Email já cadastrado.')
        return email

    class Meta:
        model = MyUser
        fields = ['email', 'turma', 'cpf', 'identidade', 'nome',
                  'logradouro', 'numero', 'complemento', 'bairro',
                  'cidade', 'uf', 'cep', 'fone1', 'fone2']
