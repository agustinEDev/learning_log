from django.shortcuts import render

def index (request):
    """La página de inicio para learning_logs."""
    return render(request, 'learning_logs/index.html')