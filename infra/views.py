from django.shortcuts import render
from django.views.generic import ListView, DetailView
from infra.models import Computer

# Create your views here.
class ComputerList(ListView):
    model = Computer
    context_object_name = "computers" # templateに渡す変数名

class ComputerDetail(DetailView):
    model = Computer
    context_object_name = "computer"