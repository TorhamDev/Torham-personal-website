from django.db import models
from utils.models import BaseModel


class IndexPage(BaseModel):

    main_text = models.TextField(
        verbose_name="index main text",
        help_text="This text is displayed on the index page"
    )
    main_text_source_link = models.URLField(
        verbose_name="Main page text source link",
        help_text="This is the link of text source."
    )
    main_text_source = models.TextField(
        verbose_name="Main page text source",
        help_text="This is the link to the main text source."
    )

    def __str__(self) -> str:
        return f"{self.main_text[0:50]}..."
