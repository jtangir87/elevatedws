from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home',
                'contact_us',
                'serv_websites',
                'port_event_dispatch',
                'port_ggrc',
                'port_lovenotevideo',
                'port_mitzvahrsvp',
                'port_catertogo',
                'port_event_xtras',
                'port_exteriordd',
                'port_sepacoldwar',
                'port_infinity_caterers',
                'port_tasty_table',
                'local_doylestown',
                'website_audit',
                ]

    def location(self, item):
        return reverse(item)
