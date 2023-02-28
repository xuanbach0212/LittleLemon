from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import MenuItem
from .serializers import MenuItemSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def MenuItemView(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data, status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def SingleMenuItemView(request):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
