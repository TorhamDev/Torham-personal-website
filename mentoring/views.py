from django.shortcuts import render
from django.views import View
from mentoring.models import MentroingPage


def get_mentoring_page_description():
    description = MentroingPage.objects.all().last()
    if description is None:
        return "Oops, there is not text :("

    return description.description


class MentoringPage(View):

    def get(self, request):
        description = get_mentoring_page_description()
        return render(
            request=request,
            template_name="mentoring.html",
            context={
                "description": description,
            }
        )

    def post(self, request):
        description = get_mentoring_page_description()
        return render(
            request=request,
            template_name="mentoring.html",
            context={
                "message": "sended",
                "description": description,
            }
        )
