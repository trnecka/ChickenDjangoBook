from chickenmessages.models import Message

def pending_messages_count(request):
    '''
    Context_processor servs variable in all page of the app. No need to add context in separate views.
    '''

    count = 0
    if request.user.is_authenticated:
        count = Message.objects.filter(recipient=request.user, status='Pending').count()
    return {'pending_messages_count': count}