from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("research/", views.research, name="research"),
    path("software/", views.software, name="software"),
    path("services/", views.services, name="services"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("contact_submitted/", views.post_contact, name="post_contact"),
]
