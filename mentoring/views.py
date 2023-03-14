from django.shortcuts import render
from django.views import View
from mentoring.models import MentroingPage, MentoringRequest


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
        
        message = "sended"
        status = 200
        try:
            #TODO : check data content. like length and etc.
            data = request.POST
            name = data.get("name")
            offered_price = int(data.get("offered_price"))
            phone_number = data.get("phone_number")
            mentor_description = data.get("mentor_description")
            

            MentoringRequest.objects.create(
                name=name,
                offered_price=offered_price,
                phone_number=phone_number,
                user_description=mentor_description,
            )
        except:
            message = "notsended"
            status = 400
        
        return render(
            request=request,
            template_name="mentoring.html",
            context={
                "message": message,
                "description": description,
            },
            status=status
        )
