from django.db import models
from django.urls import reverse
from core import models as core_models

class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    pass

class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition"""

    file = models.ImageField(upload_to="product_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)



class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    host = models.ForeignKey("users.User", related_name="rooms", on_delete=models.CASCADE)
    special_item = models.BooleanField(default=False)
    time = models.TimeField()
    item_type = models.ForeignKey("RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url

