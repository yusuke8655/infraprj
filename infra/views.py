from django.shortcuts import render
from django.views.generic import ListView
from infra.models import Computer

# Create your views here.
class ComputerList(ListView):
    model = Computer
    template_name = "infra/index.html"
    context_object_name = "computers" # templateに渡す変数名