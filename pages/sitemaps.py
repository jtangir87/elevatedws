from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'contact_us', 'port_event_dispatch', 'port_ggrc', 'port_lovenotevideo', 'port_mitzvahrsvp', 'port_catertogo', 'port_event_xtras', 'port_exteriordd', 'local_doylestown']

    def location(self, item):
        return reverse(item)
