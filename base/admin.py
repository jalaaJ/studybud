from django.contrib import admin

from .models import Room, Topic, Message, User

# We need to register the model in order to be able to see it in the admin panel
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
