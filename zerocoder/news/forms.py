from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_post_form(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        }