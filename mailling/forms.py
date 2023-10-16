from django import forms

from client.models import Client
from mailling.models import Message, Mailling


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)


class MaillingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        uid = kwargs.pop('uid')
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all().filter(owner=uid)
        self.fields['message'].queryset = Message.objects.all().filter(owner=uid)

    class Meta:
        model = Mailling
        exclude = ('owner',)
