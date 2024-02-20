from django.urls import path
from infra.views import ComputerList

urlpatterns = [
    path("", ComputerList.as_view(), name="computer_list"),
]