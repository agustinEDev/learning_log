from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registra un nuevo usuario."""
    if request.method == 'POST':
        # Muestra un formulario de registro en blanco.
        form = UserCreationForm()
    else:
        # Procesa un formulario cumplimentado.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Inicia la sesión y envía al inicio.
            login(request, new_user)
            return redirect('learning_logs:index')
        
    # Muestra un formulario en blanco o inválido.
    context = {'form': form}
    return render(request, 'registration/register.html', context)