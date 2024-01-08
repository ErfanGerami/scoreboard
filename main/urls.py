from django.urls import path
from .views import upload,scoreboard
urlpatterns = [

    path("scoreboard",scoreboard),
    path("upload",upload),
]
