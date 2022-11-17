from django.shortcuts import render


def index(request):
  context = {
    'name': 'Shu',
  }
  return render(request, 'myapp/index.html', context)
