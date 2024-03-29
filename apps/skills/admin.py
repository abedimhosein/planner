from django.contrib import admin

from .models import (
    Board,
    Queue,
    Skill,
)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    class Meta:
        model = Board

    list_display = ('title', 'user')
    list_select_related = ['user']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill

    list_display = ('title', 'order', 'parent', 'board')
    search_fields = ('title',)
    ordering = ('title',)
    list_select_related = ['parent', 'board']


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    class Meta:
        model = Queue

    list_display = ('title', 'order', 'board')
    list_select_related = ['board']
