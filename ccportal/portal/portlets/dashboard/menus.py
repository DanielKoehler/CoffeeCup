
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Dashboard",
                               reverse('portal.portlets.dashboard.views.index'),
                               weight=1,
                               icon="ios-speedometer-outline"))

