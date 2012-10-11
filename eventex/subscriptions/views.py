# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return direct_to_template(request,'subscriptions/subscription_form.html',{'form':SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return direct_to_template(request, 'subscriptions/subscription_form.html',{'form':form})

    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

def sucess(request, primary_key):
    subscription = get_object_or_404(Subscription, pk=primary_key)
    return direct_to_template(request, 'subscriptions/subscription_sucess.html',{'subscription':subscription})