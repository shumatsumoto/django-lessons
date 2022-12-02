from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
  model = Day


class AddView(generic.CreateView):
  model = Day
  form_class = DayCreateForm
  success_url = reverse_lazy('diary:index')


class UpdateView(generic.UpdateView):
  model = Day
  form_class = DayCreateForm
  success_url = reverse_lazy('diary:index')


class DeleteView(generic.DeleteView):
  model = Day
  success_url = reverse_lazy('diary:index')


# def delete(request, pk):
#   day = get_object_or_404(Day, pk=pk)
#   if request.method == 'POST':
#     day.delete()
#     return redirect('diary:index')
#   context = {
#     'day': day
#   }
#   return render(request, 'diary/day_confirm_delete.html', context)


def detail(request, pk):
  day = get_object_or_404(Day, pk=pk)
  context = {
    'day': day
  }
  return render(request, 'diary/day_detail.html', context)
