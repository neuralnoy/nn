from django.urls import path
from .views import HomepageView, AboutPageView, SolutionsPageView, ResourcesPageView, ContactPageView, CareersPageView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("solutions/", SolutionsPageView.as_view(), name="solutions"),
    path("resources/", ResourcesPageView.as_view(), name="resources"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("careers/", CareersPageView.as_view(), name="careers"),
]