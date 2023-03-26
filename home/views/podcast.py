from django.views import generic

from home.models import Podcast


class PodcastList(generic.ListView):
    model = Podcast
    context_object_name = 'podcasts'
    paginate_by = 5

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return 'podcast/add.html'
        return 'podcast/list.html'
