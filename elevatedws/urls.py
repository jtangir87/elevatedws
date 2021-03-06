"""elevatedws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogPostSitemap
sitemaps = {
    'static': StaticViewSitemap,
    'blog_posts': BlogPostSitemap
}

urlpatterns = [
    path('cms/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="sitemap"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                             content_type="text/plain"),
    ),
    path("", include("pages.urls")),
    path("blog/", include("blog.urls")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
