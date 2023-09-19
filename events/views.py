from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment

# Create your views here.

@login_required
def submit_comment(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')  # Get the event ID from the form
        event = Event.objects.get(id=event_id)  # Get the event object
        comment_text = request.POST.get('comment')  # Get the comment text from the form

        # Create a new Comment object associated with the logged-in user and the event
        Comment.objects.create(user=request.user, text=comment_text, event=event)

        return redirect('events')
    else:
        return render(request, 'comment_form.html')


def events(request):
    return render(request, 'events/events.html')

