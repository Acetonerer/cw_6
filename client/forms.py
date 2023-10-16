from django import forms

from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'
