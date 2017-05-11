from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text',"slug"]
        labels = {'text': '', "slug": 'URL'}


class EntryForm(forms.ModelForm):
    public = forms.BooleanField(required=False)
    class Meta:

        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

