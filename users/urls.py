from django.urls import path
from .views import HomepageView, AboutPageView, SolutionsPageView, ResourcesPageView, ContactPageView, CareersPageView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("solutions/", SolutionsPageView.as_view(), name="solutions"),
    path("resources/", ResourcesPageView.as_view(), name="resources"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("careers/", CareersPageView.as_view(), name="careers"),
    # Register
    path('register/', views.register, name='register'),
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Dashboard (requires login)
    path('dashboard/', views.dashboard, name='dashboard'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
]
