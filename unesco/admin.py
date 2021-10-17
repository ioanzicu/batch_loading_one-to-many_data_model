from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, State, Iso, Region


admin.site.register(Site)
admin.site.register(Category)
admin.site.register(State)
admin.site.register(Iso)
admin.site.register(Region)
