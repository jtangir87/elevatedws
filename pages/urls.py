from django.urls import path
from django.views.generic import TemplateView
from .views import contact_us

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('contact', contact_us, name="contact_us"),


    ## PORTFOLIO DETAILS ##
    path('portfolio/event-dispatch', TemplateView.as_view(
        template_name="pages/portfolio/event_dispatch.html"), name="port_event_dispatch"),
]
