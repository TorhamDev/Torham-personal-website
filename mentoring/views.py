from django.shortcuts import render
from django.views import View


class MentoringPage(View):

    def get(self, request):

        return render(
            request=request,
            template_name="mentoring.html",
            context={}
        )

    def post(self, request):

        return render(
            request=request,
            template_name="mentoring.html",
            context={
                "message": "sended",
            }
        )
