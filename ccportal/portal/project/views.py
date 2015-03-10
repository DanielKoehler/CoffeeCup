from django.shortcuts import render

# Create your views here.

def side_menu(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        menu_items = MenuItem.objects.all()
        vars = {'menu_items': menu_items}
        if kwargs:
            page, template_var = func(*args, **kwargs)
        else: page, template_var = func(*args)
        vars.update( template_var)
        return direct_to_template(request, page, vars)
    return wrapper