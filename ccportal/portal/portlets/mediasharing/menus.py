
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Media Sharing",
                               reverse('portal.portlets.mediasharing.views.index'),
                               weight=1,
                               icon="ios-albums-outline"))

