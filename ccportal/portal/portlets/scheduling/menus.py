
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

children = (


    MenuItem("Calendar",
	         reverse("portal.portlets.scheduling.views.index"),
	         weight=10,
	         icon="ios-calendar-outline"),

    MenuItem("Upcoming Events",
             reverse("portal.portlets.scheduling.views.index"),
             weight=20,
             icon="ios-list-outline"),



)

# Add two items to our main menu
Menu.add_item("sidebar", MenuItem("Scheduling",
                               reverse('portal.portlets.scheduling.views.index'),
                               weight=3,
                               icon="ios-calendar-outline", 
                               children=children))

