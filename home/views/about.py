from django.views import View
from django.shortcuts import render


class AboutView(View):

    def get(self, request):

        return render(
            request=request,
            template_name="about.html",
            context={}
        )
