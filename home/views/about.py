from django.views import View
from django.shortcuts import render
from home.models import AboutPage


def get_about_page_data():
    last = AboutPage.objects.all().last()

    if last != None:
        return last


class AboutView(View):

    def get(self, request):

        return render(
            request=request,
            template_name="about.html",
            context={}
        )
