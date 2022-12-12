from django.contrib import admin
from .models import Card
from orders.models import Order
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import path
import datetime




class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ['created', 'updated', 'paid_sum', 'card']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    fields = [('series', 'number'), ('start_date', 'end_date'), 'status', 'user', ('created', 'updated')]
    list_display = ['number', 'series', 'end_date', 'status']
    list_editable = ['status']
    inlines = [OrderInline]
    readonly_fields = ['created', 'updated']

    change_list_template = "admin/model_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('generate/', self.generate),
        ]
        return my_urls + urls

    def generate(self, request):
        print(request.POST)
        series = request.POST['series']
        quantity = int(request.POST['quantity'])
        term_dict = {'1year': datetime.datetime.now() + datetime.timedelta(days=365),
                     '6months': datetime.datetime.now() + datetime.timedelta(days=180),
                     '1month': datetime.datetime.now() + datetime.timedelta(days=31)}
        cards_by_series = Card.objects.filter(series=series)
        numbers_list = [c.number for c in cards_by_series]
        numbers_list.sort()
        print(numbers_list)
        for n in numbers_list:
            print(int(n))
        max_number = int(numbers_list[-1])
        for i in range(quantity):
            max_number += 1
            card_number = str(max_number).rjust(12, '0')
            date_end = term_dict[request.POST['datetime']]
            print(series, card_number, date_end)
            Card.objects.create(series=series, number=card_number, start_date=datetime.datetime.now(),
                                end_date=date_end, status='I', created=datetime.datetime.now())
        self.message_user(request, f'Успешно сгенерировано {quantity} карт')
        return HttpResponseRedirect("../")






