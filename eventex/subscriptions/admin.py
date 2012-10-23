#coding:utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import  ungettext, gettext as _
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name','cpf','email','phone','created_at','subscribed_today','paid',)
    date_hierarchy = ('created_at',)
    search_fields = ('name','email','phone',)
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscribed_today.boolean = True
    subscribed_today.short_descriptions = _(u'Inscrito hoje?')

    actions = ('mark_as_paid',)

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%d Inscrição foi marcada como paga.',
            u'%d Inscrições foram marcadas como pagas.',
            count
        )
        self.message_user(request, msg % count)

    mark_as_paid.short_descriptions = _(u'Marcar como pago')

admin.site.register(Subscription,SubscriptionAdmin)
