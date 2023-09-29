from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = event.comments.all()
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments})


def load_comments(request):
    """ display comment """
    event_id = request.GET.get('event_id')
    event = Event.objects.get(id=event_id)
    comments = event.comments.all()
    comments_html = render_to_string('events/comments.html', {'comments': comments})

    return JsonResponse({'comments_html': comments_html})


def events(request):
    """ return events """
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})


def submit_comment(request):
    """ post comment """
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, id=event_id)
        comment_content = request.POST.get('comment')

        comment = Comment(content=comment_content, user=request.user, event=event)
        comment.save()

        comment_data = {
            'content': comment.content,
            'user': comment.user.username,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

        return JsonResponse({'comment': comment_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)
