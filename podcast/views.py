from django.views import generic
from django.db.models import Q

from podcast.models import Podcast
from podcast import forms


class PodcastList(generic.ListView):
    model = Podcast
    context_object_name = 'podcasts'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(description__icontains=query) | Q(name__icontains=query),
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.SearchForm(self.request.GET)
        return context

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return 'podcast/add.html'
        return 'podcast/list.html'
