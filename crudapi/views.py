from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def welcome(request):
    return Response("Welcome to Django CRUD API")
