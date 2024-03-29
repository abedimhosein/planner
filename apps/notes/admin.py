from django.contrib import admin

from .models import (
    Folder,
    Note,
)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    class Meta:
        model = Folder

    list_display = ('title', 'level', 'parent')
    list_select_related = ['parent']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note

    list_display = ('title', 'summary', 'folder')
