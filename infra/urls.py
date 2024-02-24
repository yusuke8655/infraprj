from django.urls import path
from infra.views import ComputerList, ComputerDetail

app_name = 'infra'

urlpatterns = [
    path("", ComputerList.as_view(), name="list"),
    path("computer/<int:pk>/", ComputerDetail.as_view(), name="detail"),
]