from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):
    """ List Model Definiton """

    name = models.CharField(max_length=10)
    user = models.ForeignKey("users.User", related_name="lists", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", related_name="rooms", blank=True)

    def __str__(self):
        return self.name
