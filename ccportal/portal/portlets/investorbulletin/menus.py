
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem



Menu.add_item("sidebar", MenuItem("Investor Bulletin",
                               reverse('portal.portlets.investorbulletin.views.index'),
                               weight=8,
                               icon="ios-email-outline"))

