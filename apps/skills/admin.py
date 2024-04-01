from admin_searchable_dropdown.filters import AutocompleteFilterFactory
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
    search_fields = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user = request.user
        if user.is_superuser:
            return qs

        return qs.filter(user=user)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill

    list_display = ('title', 'order', 'parent', 'board')
    list_filter = [
        AutocompleteFilterFactory('Board', 'board'),
        AutocompleteFilterFactory('Top-Level Skill', 'parent'),
    ]
    search_fields = ('title',)
    ordering = ('title',)
    list_select_related = ['parent', 'board']

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user = request.user
        if user.is_superuser:
            return qs

        return qs.filter(board__user=user)


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    class Meta:
        model = Queue

    list_display = ('title', 'order', 'board')
    list_select_related = ['board']

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user = request.user
        if user.is_superuser:
            return qs

        return qs.filter(board__user=user)
