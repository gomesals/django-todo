from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_complete')
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'is_complete': 'Finalizada?'
        }
