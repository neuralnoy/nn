from django.urls import path
from .views import HomepageView, AboutPageView, SolutionsPageView, ResourcesPageView, ContactPageView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("solutions/", SolutionsPageView.as_view(), name="solutions"),
    path("resources/", ResourcesPageView.as_view(), name="resources"),
    path("contact/", ContactPageView.as_view(), name="contact"),
]