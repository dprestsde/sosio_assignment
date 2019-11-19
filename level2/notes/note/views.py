from django.shortcuts import render

# Create your views here.
from .models import Notes
from rest_framework import views
from  rest_framework.response import Response
from rest_framework import status
from .serializers import NotesSerializer
from django.http import JsonResponse

class CreateNotes(views.APIView):
    def post(self, request):
        

        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            model = Notes(title=title, description=description)
            model.save()
            print("#########")
            return Response("Data has been succesfully created" , status=status.HTTP_201_CREATED)
            
        else:
            return Response("Error Occured" , status=status.HTTP_400_BAD_REQUEST)

class UpdateNotes(views.APIView):
    def post(self, request):
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            all_objects =  Notes.objects.all()
            model = all_objects.get(title=title)
            print("***********")
            model.description = description
            print(model.description)
            print(model.title)
            model.save()
            print(model.description)

            return Response("Data has successfully Updated" , status=status.HTTP_201_CREATED)
            
        else:
            return Response("Error Occured" , status=status.HTTP_400_BAD_REQUEST)

class DeleteNotes(views.APIView):
    def post(self, request):
        if request.method == "POST":
            title = request.POST["title"]
            all_objects =  Notes.objects.all()
            model = all_objects.get(title=title)
            print("***********")
            
            print(model.description)
            print(model.title)
            model.delete()
            print(model.description)

            return Response("Data has successfully deleted" , status=status.HTTP_201_CREATED)
            
        else:
            return Response("Error Occured" , status=status.HTTP_400_BAD_REQUEST)

class ViewNotes(views.APIView):
    def post(self, request):
        if request.method == "POST":
            title = request.POST["title"]
            print("########", title)
            print(request.POST)
            all_objects =  Notes.objects.all()
            model = all_objects.get(title=title)
            print("***********")
        
            print(model.description)
            print(model.title)
            print(model.description)
            view_dict = {
                "title": model.title,
                "description": model.description,
                "creation time": model.creation_time,
                "last updated at": model.updated_at
            }
            return JsonResponse(view_dict, safe=False, status=status.HTTP_201_CREATED)
            
        else:
            return Response("Error Occured" , status=status.HTTP_400_BAD_REQUEST)
