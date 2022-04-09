from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Code


class CodeView(ListView):
    model = Code
    template_name = "skulpt.html"
    context_object_name = "all_code"

