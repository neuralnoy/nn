from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect

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

class CareersPageView(TemplateView):
    template_name = "careers.html"
