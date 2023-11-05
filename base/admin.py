from django.contrib import admin

from .models import Room, Topic, Message

# We need to register the model in order to be able to see it in the admin panel
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
