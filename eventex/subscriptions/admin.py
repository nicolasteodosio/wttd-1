#coding:utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import gettext as _
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name','cpf','email','phone','created_at','subscribed_today',)
    date_hierarchy = ('created_at',)
    search_fields = ('name','email','phone',)
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscribed_today.boolean = True
    subscribed_today.short_descriptions = _(u'Inscrito hoje?')

admin.site.register(Subscription,SubscriptionAdmin)
