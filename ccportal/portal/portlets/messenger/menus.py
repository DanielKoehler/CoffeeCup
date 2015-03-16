
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Messenger",
                               reverse('portal.portlets.messenger.views.index'),
                               weight=4,
                               icon="ios-chatbubble-outline"))

