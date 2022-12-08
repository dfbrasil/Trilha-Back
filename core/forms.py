from django import forms

from django.core.mail import send_mail

# from empresa import settings

class ContatoForm(forms.Form):

    name = forms.CharField(
        label = 'Nome:',
        required=True,
    )

    email = forms.EmailField(
        label='Email:',
    )

    mensagem = forms.CharField(
        label = 'Mensagem:',
        widget=forms.Textarea(),
        required=True, #true já é default
    )

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        mensagem = f'Nome: {name}\nemail: {email} \n mensagem {mensagem}'
        # send_mail(
        #     'Contato do Djanogo e-commerce', mensagem, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL]
        # )

    # def __init__(self, *args, **kwargs):
    #     super(ContatoForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['mensagem'].widget.attrs['class'] = 'form-control'