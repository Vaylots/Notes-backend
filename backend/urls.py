from django.contrib import admin
from django.urls import path
from Notes import views as NoteViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("getallnotes/", NoteViews.GetAllNotes),
    path("getnote/<int:id>", NoteViews.GetNote),
    path("deletenote/<int:id>", NoteViews.DeleteNote),
    path("addnote/", NoteViews.addNote),
    path("successnote/<int:id>", NoteViews.successNote),
]
