from django.shortcuts import render
from django.http import HttpResponse
# def home_page_view(request):
#     return HttpResponse("Hello, World!")

from django.views.generic import TemplateView

class HomePageView (TemplateView):
    template_name = "resume.html"
