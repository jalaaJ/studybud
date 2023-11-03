from django.shortcuts import render

rooms = [
    {"id": 1, "name": "Let's learn Python!"},
    {"id": 2, "name": "Design with me"},
    {"id": 3, "name": "Frontend developers"},
]


# Create your views here.
def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    for each_room in rooms:
        if each_room["id"] == int(pk):
            room = each_room
    context = {"room": room}
    return render(request, "base/room.html", context)
