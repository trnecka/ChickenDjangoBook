from accounts.models import Message

def pending_messages_count(request):
    if request.user.is_authenticated:
        count = Message.count_pending_messages()
        return {'pending_messages_count': count}
    return {'pending_messages_count': 0}