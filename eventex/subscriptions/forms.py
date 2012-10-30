# -*- coding:utf-8 -*-
from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription



def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))

def clean(self):
    super(SubscriptionForm, self).clean()

    if not self.cleaned_data.get('email') and \
       not self.cleaned_data.get('cpf'):
        raise ValidationError(_(u'Informe seu e-mail ou telefone'))

    return self.cleaned_data


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args,**kwargs)

        self.fields['cpf'].validators.append(CPFValidator)