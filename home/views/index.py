from django.views import View
from django.shortcuts import render
from home.models import IndexPage


class IndexView(View):

    def get(self, request):
        index_page_data = IndexPage.objects.all().last()

        return render(
            request=request,
            template_name="index.html",
            context={
                "index_data": index_page_data,
            }
        )
