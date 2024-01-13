from chickenmessages.models import Message

def pending_messages_count(request):
    count = 0
    if request.user.is_authenticated:
        count = Message.objects.filter(recipient=request.user, status='Pending').count()
    return {'pending_messages_count': count}