from django.urls import path
from django.views.generic import TemplateView
from .views import contact_us

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('contact', contact_us, name="contact_us"),


    ## PORTFOLIO DETAILS ##
    path('portfolio/event-dispatch-employee-scheduling-app', TemplateView.as_view(
        template_name="pages/portfolio/event_dispatch.html"), name="port_event_dispatch"),
    path('portfolio/ggrc-info-site', TemplateView.as_view(
        template_name="pages/portfolio/ggrcleaners.html"), name="port_ggrc"),
    path('portfolio/love-note-video-interactive-web-application', TemplateView.as_view(
        template_name="pages/portfolio/lovenotevideo.html"), name="port_lovenotevideo"),
]
