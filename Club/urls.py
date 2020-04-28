from django.urls import path
from .views import StateList, ClubList

urlpatterns = [
    path("states/", StateList.as_view(), name="State_List"),
    path("states/<slug:state_slug>/", ClubList.as_view(), name="Club_List")
]
