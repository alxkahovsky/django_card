from django.contrib import admin
from .models import Card
from orders.models import Order
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError



class CardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['full_number'].initial = 'asadasdasd'
        print(self.fields['full_number'])
        print(self.instance.number)
        model = Card
        fields = ['series', 'number', 'full_number', 'start_date', 'end_date', 'status', 'user', 'created']
        widgets = {'full_number': forms.HiddenInput()}


    # def save(self, commit=True):
    #     print('-----------------------------------------------')
    #     raise ValidationError("Please enter valid date. Either today's date or after that.")
    #     data = self.cleaned_data
    #     # user = User(email=data['email'], first_name=data['first_name'],
    #     #             last_name=data['last_name'], password1=data['password1'],
    #     #             password2=data['password2'])
    #     # user.save()
    #     # userProfile = UserProfile(user=user, gender=data['genger'],
    #     #                           year=data['year'], location=data['location'])
    #     # userProfile.save()
    #     print(data)


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ['created', 'updated', 'paid_sum', 'card']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # fields = [('series', 'number'), 'full_number', ('start_date', 'end_date'), 'status', 'user', ('created', 'updated')]
    # list_display = ['id', 'full_number', 'end_date', 'status']
    # list_editable = ['status']
    # inlines = [OrderInline]
    # readonly_fields = ['full_number', 'created', 'updated']
    model = Card
    form = CardForm
    # prepopulated_fields = {'full_number': ('series', 'number')}

    # def save_model(self, request, obj, form, change):
    #     print('aaaaaaaaaaaaaaaaaaaaa')
    #     print(form.changed_data)
    #     messages.error(request, 'Car has been sold')
    #     super(CardAdmin, self).save_model(request, obj, form, change)
    #     raise ValidationError("Please enter valid date. Either today's date or after that.")
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     try:
    #         print(object_id)
    #         if object_id is not None:
    #             card = Card.objects.get(id=object_id)
    #             card.full_number = f'{card.series}{card.number}'
    #             card.save()
    #         return super(CardAdmin, self).changeform_view(request, object_id, form_url, extra_context)
    #     except IntegrityError as e:
    #         self.message_user(request, e, level=messages.ERROR)
    #         if object_id is not None:
    #             card = Card.objects.get(id=object_id)
    #             # card.delete()
    #         return redirect(form_url)







