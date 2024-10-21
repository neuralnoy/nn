from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('dashboard')  # Redirect to dashboard after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')  # Custom dashboard for logged-in users
