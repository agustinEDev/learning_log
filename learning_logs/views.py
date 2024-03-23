from django.shortcuts import render
from .models import Topic

def index (request):
    """La página de inicio para learning_logs."""
    return render(request, 'learning_logs/index.html')

def topics (request):
    """Muestra todos los temas."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic (request, topic_id):
    """Muestra un tema concreto y todas sus entradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)