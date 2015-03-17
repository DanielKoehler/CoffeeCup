
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

children = (

    MenuItem("Users",
             reverse("portal.portlets.useradministration.views.users"),
             weight=10,
             icon="ios-person-outline"),

    MenuItem("User Groups",
             reverse("portal.portlets.useradministration.views.groups"),
             weight=80,
             icon="ios-list-outline"),

)

# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("User Administration",
                               reverse('portal.portlets.useradministration.views.users'),
                               weight=7,
                               icon="ios-people-outline",
                               children=children))
