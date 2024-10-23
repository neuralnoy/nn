from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.conf import settings
import boto3
from .forms import ContactForm


class HomepageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class SolutionsPageView(TemplateView):
    template_name = "solutions.html"

class ResourcesPageView(TemplateView):
    template_name = "resources.html"

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



class ContactPageView(FormView):
    template_name = "contact.html"  # Your template
    form_class = ContactForm
    success_url = reverse_lazy('contact')  # Redirects to contact page after success

    def form_valid(self, form):
        # Get form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        # Create an SES client
        ses_client = boto3.client(
            'ses',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_SES_REGION_NAME
        )

        # Send email
        try:
            ses_client.send_email(
                Source='info@neuralnoy.com',  # Your verified email
                Destination={
                    'ToAddresses': ['info@neuralnoy.com'],  # Recipient email
                },
                Message={
                    'Subject': {
                        'Data': f'Contact Form Submission from {name}',
                        'Charset': 'UTF-8'
                    },
                    'Body': {
                        'Text': {
                            'Data': f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                            'Charset': 'UTF-8'
                        }
                    }
                }
            )
            messages.success(self.request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(self.request, f'Failed to send email: {str(e)}')

        return super().form_valid(form)
