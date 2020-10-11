from django.urls import path
from django.views.generic import TemplateView
from .views import contact_us, consultation_form

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('contact', contact_us, name="contact_us"),
    path('consultation-request', consultation_form, name="consultation_form"),
    path('client-connect', TemplateView.as_view(
        template_name="pages/sendible_client_connect.html"), name="client_connect"),


    ## PORTFOLIO DETAILS ##
    path('portfolio/event-dispatch-employee-scheduling-app', TemplateView.as_view(
        template_name="pages/portfolio/event_dispatch.html"), name="port_event_dispatch"),
    path('portfolio/ggrc-info-site', TemplateView.as_view(
        template_name="pages/portfolio/ggrcleaners.html"), name="port_ggrc"),
    path('portfolio/love-note-video-interactive-web-application', TemplateView.as_view(
        template_name="pages/portfolio/lovenotevideo.html"), name="port_lovenotevideo"),
    path('portfolio/event-rsvp-custom-web-application', TemplateView.as_view(
        template_name="pages/portfolio/mitzvahrsvp.html"), name="port_mitzvahrsvp"),
    path('portfolio/catertogo-e-commerce-platform', TemplateView.as_view(
        template_name="pages/portfolio/catertogo.html"), name="port_catertogo"),
    path('portfolio/event-xtras', TemplateView.as_view(
        template_name="pages/portfolio/eventxtras.html"), name="port_event_xtras"),
    path('portfolio/exterior-design-and-development', TemplateView.as_view(
        template_name="pages/portfolio/exteriordd.html"), name="port_exteriordd"),


    ## LOCAL LANDING PAGES ##
    path('doylestown-website-design', TemplateView.as_view(
        template_name="pages/local/doylestown.html"), name="local_doylestown"),


]
