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

    search_fields = ('title',)
    list_display = ('title',)
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