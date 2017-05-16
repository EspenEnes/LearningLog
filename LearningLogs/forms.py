from django import forms
from .models import Topic, Entry, Comments

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    public = forms.BooleanField(required=False)
    class Meta:

        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text',]
        labels = {'text': 'Write your comment'}

