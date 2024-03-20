from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note

    list_display = ('summary',)
