from django.db import models
from utils.models import BaseModel
from django.core.validators import FileExtensionValidator


class Podcast(BaseModel):
    name = models.CharField(
        max_length=100,
        help_text="podcast name",
    )
    cover = models.ImageField(
        upload_to="covers/",
        help_text="podcast cover",
    )
    description = models.TextField(
        help_text='podcast description',
    )
    file = models.FileField(
        upload_to='audios/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'mp3',
                    'wav',
                    'ogg',
                    'm4a',
                ]
            )
        ],
        help_text='podcast audio file',
    )

    class Meta:
        ordering = (
            '-updated_at',
        )

    def __str__(self) -> str:
        return self.name
