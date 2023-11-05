from django.db import models


class Room(models.Model):
    # host =

    # topic =

    name = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True)

    # participants =

    # takes a timestamp everytime that we save
    updated = models.DateTimeField(auto_now=True)

    # takes a timestamp when we create the room
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
