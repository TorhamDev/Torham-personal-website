from django.views import View
from django.shortcuts import render
from home.models import IndexPage


class IndexView(View):

    def get(self, request):
        index_page_data = IndexPage.objects.all().last()
        if index_page_data != None:
            context = {
                "main_text_source_link": index_page_data.main_text_source_link,
                "main_text_source": index_page_data.main_text_source,
                "main_text": index_page_data.main_text
            }
        else:
            context = {
                "main_text_source_link": "#",
                "main_text_source": "torham",
                "main_text": "Hello, World!",
            }

        return render(
            request=request,
            template_name="index.html",
            context=context
        )
