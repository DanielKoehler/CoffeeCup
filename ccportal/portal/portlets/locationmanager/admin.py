from django.contrib import admin

from models import Location, Photo


# class Location(Location):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field

    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name', 'role')}),
    # )
    
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2')}
    #     ),
    # )

    # form = UserChangeForm
    # add_form = UserCreationForm
    # list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('email', 'first_name', 'last_name')
    # ordering = ('email',)

admin.site.register(Location)
admin.site.register(Photo)

