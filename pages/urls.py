from django.urls import path
from django.views.generic import TemplateView
from .views import home_view, contact_us, consultation_form, website_service

urlpatterns = [
    path('', home_view, name="home"),
    path('contact', contact_us, name="contact_us"),
    path('consultation-request', consultation_form, name="consultation_form"),
    path('client-connect', TemplateView.as_view(
        template_name="pages/sendible_client_connect.html"), name="client_connect"),

    ## SERVICE PAGES ##
    path('website-design', website_service, name="serv_websites"),


    ## PORTFOLIO DETAILS ##
    path('portfolio/laura-silverstein-blog-website-design', TemplateView.as_view(
        template_name="pages/portfolio/laurasilverstein.html"), name="port_laurasilverstein"),
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
    path('portfolio/sepa-cold-war-historical-society-website-design', TemplateView.as_view(
        template_name="pages/portfolio/sepacoldwar.html"), name="port_sepacoldwar"),
    path('portfolio/infinity-caterers-website-design', TemplateView.as_view(
        template_name="pages/portfolio/infinity_caterers.html"), name="port_infinity_caterers"),
    path('portfolio/tasty-table-market-website-design', TemplateView.as_view(
        template_name="pages/portfolio/tasty_table.html"), name="port_tasty_table"),


    ## LOCAL LANDING PAGES ##
    path('doylestown-website-design', TemplateView.as_view(
        template_name="pages/local/doylestown.html"), name="local_doylestown"),


    ## ADVERTISING LANDING PAGES ##
    path('website-seo-audit', TemplateView.as_view(
        template_name="pages/landing/site_audit.html"), name="website_audit"),

]
