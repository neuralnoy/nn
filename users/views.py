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

    def post(self, request, *args, **kwargs):
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        try:
            send_mail(
                f'New message from {name}',
                message,
                email,  # sender's email
                ['info@neuralnoy.com'],  # recipient's email
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the contact page after success
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return self.render_to_response(self.get_context_data())

class CareersPageView(TemplateView):
    template_name = "careers.html"
