from django.http import JsonResponse
from .models import NotesController

# Create your views here.


def GetAllNotes(request):

    Notes = list(NotesController.objects.values())
    return JsonResponse(Notes, safe=False)


def GetNote(request, id):

    Note = list(NotesController.objects.filter(id=id).values())
    return JsonResponse(Note, safe=False)


def addNote(request):
    title = request.POST.get("Title")
    Note = NotesController(title=title)
    Note.save()

    return JsonResponse({"message": f"note <{title}> has been added"})


def successNote(request, id):
    Note = NotesController.objects.get(id=id)
    Note.success = True
    Note.save()

    return JsonResponse({"message": f"note <{Note.title}> has been successed"})


def DeleteNote(request, id):
    Note = NotesController.objects.get(id=id)
    Note.delete()
    return JsonResponse({"message": "Note has been deleted"})
