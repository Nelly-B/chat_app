from django.urls import path, re_path

from chat.views import index, room

appname = 'chat'

urlpatterns = [
    path("", index, name="index"),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name="room"),
]