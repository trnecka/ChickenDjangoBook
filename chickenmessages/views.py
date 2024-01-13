from django.shortcuts import render,redirect, get_object_or_404
from chickenmessages.forms import MessageForm
from accounts.models import User
from chickenmessages.models import Message
from django.contrib import messages

def send_message(request, recipient):
    card = get_object_or_404(User, pk=recipient)

    # Initialize the form with sender's name and email if the user is logged in
    if request.user.is_authenticated:
        initial_data = {
            'sender_name': request.user.get_full_name(),  # Or just request.user.first_name
            'sender_email': request.user.email
        }
        message_form = MessageForm(initial=initial_data)
    else:
        message_form = MessageForm()

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.recipient = card
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('chicken-book')  # Replace 'some_view' with the desired redirect view name
        else:
            messages.error(request, 'There was an error in your form.')

    context = {'messageform': message_form, 'card': card}
    return render(request, 'send_message.html', context)

def message_list(request):
    messages = Message.objects.filter(recipient=request.user)
    context = {'private_messages': messages }
    return render(request, 'message_list.html', context)

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Update the message status to 'Read' if it is 'Pending'
    if message.status == 'Pending':
        message.status = 'Read'
        message.save()

    return render(request, 'message_detail.html', {'message': message})
