from django.db import models
from utils.models import BaseModel


class IndexPage(BaseModel):

    main_text = models.TextField(
        verbose_name="index main text",
        help_text="This text is displayed on the index page"
    )
    main_text_source = models.URLField(
        verbose_name="Main page text source",
        help_text="This is the link to the main text source."
    )