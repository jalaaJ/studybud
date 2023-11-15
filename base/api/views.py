from django.http import JsonResponse


# Allow clients to access the rooms through these apis
def getRoutes(request):
    routes = ["GET /api", "GET /api/rooms", "GET /api/rooms/:id"]
    return JsonResponse(routes, safe=False)
