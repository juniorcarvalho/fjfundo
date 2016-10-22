from django import forms
from django.contrib.auth import authenticate
from fjfundo.core.models import MyUser, PasswordReset
from fjfundo.core.utils import generate_hash_key


class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail', required=True)
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
            raise forms.ValidationError("Acesso não autorizado.")
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
        fields = ['email', 'cpf', 'identidade', 'nome',
                  'logradouro', 'numero', 'complemento', 'bairro',
                  'cidade', 'uf', 'cep', 'fone1', 'fone2']


class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuário encontrado com este e-mail.'
        )

    def save(self):
        email = self.cleaned_data['email']
        user = MyUser.objects.get(email=email)
        key = generate_hash_key(user.email)
        reset = PasswordReset(key=key, user=user)
        reset.save()

        # envio de email...

