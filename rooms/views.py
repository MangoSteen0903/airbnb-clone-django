from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def view_all_rooms(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
        },
    )


def view_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        return render(
            request,
            "room_detail.html",
            {
                "room": room,
            },
        )

    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
            },
        )
