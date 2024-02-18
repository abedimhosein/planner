from typing import Any
from django.contrib import admin
from .models import (
    Course,
    Note,
    ProgressLog,
    Part,
)
from admin_searchable_dropdown.filters import AutocompleteFilter


class SkillFilter(AutocompleteFilter):
    title = 'Skill' # display title
    field_name = 'skill' # name of the foreign key field



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

    list_display = ('title', 'skill')
    list_editable = ('skill',)
    list_per_page = 10
    search_fields = ('title', )
    list_filter = [SkillFilter]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    class Meta:
        model = Part

    list_display = ('title', 'order')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note

    list_display = ('summary',)


@admin.register(ProgressLog)
class ProgressLogAdmin(admin.ModelAdmin):
    class Meta:
        model = ProgressLog

    list_display = ('summary',)
