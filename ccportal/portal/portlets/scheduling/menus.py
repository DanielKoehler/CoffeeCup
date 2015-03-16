
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Scheduling",
                               reverse('portal.portlets.scheduling.views.index'),
                               weight=3,
                               icon="ios-calendar-outline"))

