"""Define patrones de URL para learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Página de inicio
    path('', views.index, name = 'index'),
    #Página que muestra todos los temas
    path('topics', views.topics, name = 'topics'),
    # Página de detalles para un tema individual
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # Página para añadir un tema nuevo
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # Página para añadir una nueva entrada
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # Página para editar una entrada
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]