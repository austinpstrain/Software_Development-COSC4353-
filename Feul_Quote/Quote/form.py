from django.forms import ModelForm
from .models import *


class GetquoteForm(ModelForm):
    class Meta:
        model = Getquote
        fields = ['customer', 'gallons_requested', 'Address_1', 'state',
                  'delivery_date', 'suggested_price']
