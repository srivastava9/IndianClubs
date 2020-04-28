from django.contrib import admin
from .models import Club, State
# Register your models here.


class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields = ("slug",)


admin.site.register(State, StateAdmin)


class ClubAdmin(admin.ModelAdmin):
    list_display = ("Name", "League", "State", "City")
    search_fields = ["Name", "State__name", "City"]
    list_filter = ("State", "League", "City")


admin.site.register(Club, ClubAdmin)
