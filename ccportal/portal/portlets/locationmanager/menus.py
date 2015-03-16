
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Location Manager",
                               reverse('portal.portlets.locationmanager.views.index'),
                               weight=5,
                               icon="ios-navigate-outline"))