from django.db import models
from utils.models import BaseModel


class AboutPage(BaseModel):
    description = models.TextField(
        help_text="The text will be displayed on the About Us page."
    )
    about_profile = models.ImageField(
        help_text="The photo will be displayed on the About Us page."
    )

    # social links
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    github_link = models.URLField()
    telegram_link = models.URLField()
    email = models.EmailField()
