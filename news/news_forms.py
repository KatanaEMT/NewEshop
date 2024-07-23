from django import forms
from .models import New


class DatePicker(forms.DateInput):
    input_type = 'date'


class NewsForm(forms.ModelForm):
    guarantee = forms.DateField(
        widget=DatePicker,
        label="День публикации",
        required=False,
    )

    class Meta:
        model = New
        fields = [
            'title',
            'article',
            'views_qty',
            'category',
            'guarantee',
        ]