from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """Review Model Definition """

    review = models.TextField()
    신선도 = models.IntegerField()
    배송 = models.IntegerField()
    가격 = models.IntegerField()
    품질 = models.IntegerField()
    정확성 = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name = "reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):

        avg = (self.신선도 + self.배송 + self.가격 + self.품질 + self.정확성) / 5
        return round(avg, 2)
