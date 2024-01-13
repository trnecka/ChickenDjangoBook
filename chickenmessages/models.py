from django.db import models
from django.conf import settings

class Message(models.Model):
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read')
    )
    
    sender_name = models.CharField(max_length=100, blank=True, null=True)  # Sender's email, optional if the sender is logged in
    sender_email = models.EmailField(blank=True, null=True)  # Sender's email, optional if the sender is logged in
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')  # Recipient of the message
    subject = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)  # Message content
    sent_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message is sent
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')