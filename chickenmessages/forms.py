from django import forms
from chickenmessages.models import Message

# Msg form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'sender_email', 'subject', 'content']