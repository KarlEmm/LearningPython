from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
  if request.method != 'POST':
    # No data submitted, generate a blank form.
    form = UserCreationForm()
  else:
    # POST request; process data.
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      login(request, new_user)
      return redirect('blogs:index')
  
  # Display an invalid or a blank form.
  context = {'form': form}
  return render(request, 'registration/register.html', context)

