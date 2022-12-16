from django.db.models import Q
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    model = Post
    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(text__icontains=keyword))
        return queryset