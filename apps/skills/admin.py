from django.contrib import admin

from .models import (
    Queue,
    Skill,
    Board,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill

    list_display = ('title', 'board', 'parent')
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    class Meta:
        model = Queue

    list_display = ('title',)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    class Meta:
        model = Board

    list_display = ('title',)
