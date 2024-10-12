from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class SolutionsPageView(TemplateView):
    template_name = "solutions.html"

class ResourcesPageView(TemplateView):
    template_name = "resources.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

