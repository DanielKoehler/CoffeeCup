
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

children = (

    MenuItem("Check In/Out",
             # reverse("portal.portlets.equipmentmanager.views.check"),
             '#',
             weight=10,
             icon="ios-barcode-outline"),

    MenuItem("Equipment",
	         reverse("portal.portlets.equipmentmanager.views.index"),
	         weight=80,
	         icon="ios-upload-outline"),

)

Menu.add_item("sidebar", MenuItem("Equipment Manager",
                               reverse('portal.portlets.equipmentmanager.views.index'),
                               weight=6,
                               icon="ios-videocam-outline",
                               children=children))

