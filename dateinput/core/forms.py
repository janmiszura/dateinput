from django.forms import ModelForm, DateInput
from core.models import Entity


class DateInputCustom(DateInput):
    input_type = 'date'


class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = ['date_type_text', 'date_type_date']
        widgets = {
            'date_type_text': DateInput(format=('%Y/%m/%d')),
            'date_type_date': DateInputCustom(),
        }