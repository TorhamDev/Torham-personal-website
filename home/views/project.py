from django.views import View
from django.shortcuts import render
from home.models import ProjectPage


class ProjectView(View):

    def get(self, request):

        all_project = ProjectPage.objects.all()

        return render(
            request=request,
            template_name="project.html",
            context={
                "projects": all_project,
            }
        )
