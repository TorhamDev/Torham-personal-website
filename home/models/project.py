from django.db import models
from utils.models import BaseModel
from utils.choices import PROJECT_LOCATIONS, PROJECT_LOCATION_GITHUB


class ProjectPage(BaseModel):
    project_name = models.CharField(
        max_length=100,
        help_text="project name",
    )
    project_description = models.TextField(
        help_text="project description",
    )
    project_link = models.URLField(
        help_text="project link. (github repo link or other lications)"
    )
    project_location = models.CharField(
        max_length=2,
        choices=PROJECT_LOCATIONS,
        default=PROJECT_LOCATION_GITHUB,
        help_text=""
    )

    def __str__(self) -> str:
        return self.project_name