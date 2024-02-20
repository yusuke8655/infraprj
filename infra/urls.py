from django.urls import path
from infra.views import ComputerList, ComputerDetail

urlpatterns = [
    path("", ComputerList.as_view(), name="computer_list"),
    path("computer/<int:pk>/", ComputerDetail.as_view(), name="computer_detail"),
]