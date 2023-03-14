from django.db import models
from utils.models import BaseModel


class MentoringRequest(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    offered_price = models.BigIntegerField()
    user_description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class MentroingPage(BaseModel):
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.description[0:60]}..."
