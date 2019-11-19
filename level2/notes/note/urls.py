from django.urls import path
from .views import CreateNotes, UpdateNotes, DeleteNotes, ViewNotes

urlpatterns = [
  path('create/', CreateNotes.as_view()),
  path('update/', UpdateNotes.as_view()),
  path('delete/', DeleteNotes.as_view()),
  path('get/', ViewNotes.as_view())
]