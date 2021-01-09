from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "성별",
                    "인증_회원",
                    "전화번호",
                )
            },
        ),

    )

    list_filter = UserAdmin.list_filter + ("인증_회원",)




    list_display = ("username", "성별", "인증_회원", "전화번호", "email",)
