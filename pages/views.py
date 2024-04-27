from colorama import Fore, Style
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import FullEnquiryForm, SimpleEnquiryForm
from .models import FullEnquiry, SimpleEnquiry

# Create your views here.

def home(request : HttpRequest) -> HttpResponse:
    """
    Render out our home page template.
    """
    context = {
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "About", "url": "/about/"},
            {"name": "Services", "url": "/services/"},
            {"name": "Contact", "url": "/contact/"},
        ]
    }

    return render(request, "pages/home.html",context)

def about(request):
    return render(request, "pages/about.html")

def services(request):
    return render(request, "pages/services.html")

def research(request):
    return render(request, "pages/research.html")

def software(request):
    return render(request, "pages/software.html")

def blog(request):
    return render(request, "pages/blog.html")

class ContactView(View):
    """
    Handles people trying to get in touch.
    """
    def get(self, request : HttpRequest) -> HttpResponse:
        """
        Render out a blank contact form.
        """
        form = SimpleEnquiryForm()

        context = {
            "form" : form,
        }

        return render(request, "pages/contact.html", context)

    def post(self, request :HttpRequest) -> HttpResponse:
        """
        Handles submission of the contact form.
        """

        print(f"{Fore.GREEN}: {request.POST} {Style.RESET_ALL}")

        form = SimpleEnquiryForm(request.POST)

        context = {
            "form" : form,
        }

        if form.is_valid():
            form.save()
            context["success"] = True
            # Return a redirect to the post contact page
            return redirect("pages:post_contact")

        return render(request, "pages/contact.html", context)

def post_contact(request : HttpRequest) -> HttpResponse:
    """
    After submitting a contact request, we redirect to this page. It is just
    going to have a little placeholder message - something like 
    'Thanks for getting in touch, we'll get back to you soon'.
    And a link back to the home page.
     
    """

    return render(request, "pages/post_contact.html")

def enquiry(request):

    form = FullEnquiryForm()

    context = {
        "form" : form,
    }

    if request.method == "POST":
        raise NotImplementedError("Full enquiry form submission not implemented yet.")

    return render(request, "pages/contact.html", context)
