from django.contrib import admin
from .models import (
    Course,
    Note,
    ProgressLog,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

    list_display = ('title',)


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
