from django.contrib import admin

from .models import Room

# We need to register the model in order to be able to see it in the admin panel
admin.site.register(Room)
