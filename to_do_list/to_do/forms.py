from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from to_do.choice_config import CHOICES


class TaskForm(forms.Form):
    task_text = forms.CharField(max_length=200, required=True, label='Название задачи',
                                widget=forms.TextInput({'class': 'form-input'}))
    task_description = forms.CharField(max_length=2000, required=True, label='Описание',
                                       widget=widgets.Textarea)
    state = forms.ChoiceField(choices=CHOICES, label='Состояние')
    deadline = forms.DateField(required=False, widget=widgets.SelectDateWidget, label='Дедлайн')

    def clean_task_text(self):
        task_text = self.cleaned_data.get('task_text')
        if len(task_text) < 2:
            raise ValidationError('Поле должно быть заполнено более чем одним символом')
        return task_text
