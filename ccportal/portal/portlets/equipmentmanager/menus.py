
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Equipment Manager",
                               reverse('portal.portlets.equipmentmanager.views.index'),
                               weight=6,
                               icon="ios-videocam-outline"))

