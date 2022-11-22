from django.shortcuts import render, redirect
from .forms import DayCreateForm


def index(request):
  return render(request, 'diary/day_list.html')


def add(request):
  form = DayCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('diary:index')
  context = {
    'form': form
  }

  return render(request, 'diary/day_form.html', context)
