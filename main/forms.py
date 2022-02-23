from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender_login', 'email', 'topic_letter', 'text_message']

