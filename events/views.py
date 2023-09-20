from django.shortcuts import render, redirect
from .models import Event, Comment
from django.contrib.auth.decorators import login_required

def events(request):
    # Fetch events and their related comments
    events = Event.objects.all()
    print(events)  # Add this line for debugging
    return render(request, 'events/events.html', {'events': events})

@login_required
def submit_comment(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = Event.objects.get(id=event_id)
        comment_content = request.POST.get('comment')

        comment = Comment(content=comment_content, user=request.user, event=event)
        comment.save()

        return redirect('events')
    else:
        return render(request, 'comment_form.html')  
