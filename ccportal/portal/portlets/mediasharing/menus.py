
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

children = (

    MenuItem("Files",
             reverse("portal.portlets.mediasharing.views.index"),
             weight=10,
             icon="ios-cloud-outline"),

    MenuItem("Shared",
	         reverse("portal.portlets.mediasharing.views.index"),
	         weight=80,
	         icon="ios-upload-outline"),

    MenuItem("Favorites",
	         reverse("portal.portlets.mediasharing.views.index"),
	         weight=80,
	         icon="ios-star-outline"),

)

Menu.add_item("sidebar", MenuItem("Media Sharing",
                               reverse('portal.portlets.mediasharing.views.index'),
                               weight=1,
                               icon="ios-albums-outline", 
                               children=children))

