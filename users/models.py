from django.db import models
from django.contrib.auth.models import AbstractUser
#-*- coding:utf-8 -*-


class User(AbstractUser):

    """ Custom User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "제3의 성"),
    )
    전화번호 = models.CharField(max_length=13, default="")
    프로필 = models.TextField(blank=True)
    프로필_사진 = models.ImageField(blank=True, null=True, upload_to="avatars")
    성별 = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, default="")
    생일 = models.DateField(blank=True, null=True)
    인증_회원 = models.BooleanField(default=False)

