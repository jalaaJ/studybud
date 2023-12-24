from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


# Allow clients to access the rooms through these apis
@api_view(["GET"])
def getRoutes(request):
    routes = ["GET /api", "GET /api/rooms", "GET /api/rooms/:id"]
    return Response(routes)


@api_view(["GET"])
def getRooms(request):
    rooms = Room.objects.all()

    # many=True because we're returning more than one value
    serilizer = RoomSerializer(rooms, many=True)
    return Response(serilizer.data)


@api_view(["GET"])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serilizer = RoomSerializer(room, many=False)
    return Response(serilizer.data)
