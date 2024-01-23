from django.contrib import admin
from .models import (
    Queue,
    Skill,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill

    list_display = ('title',)





@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    class Meta:
        model = Queue

    list_display = ('title',)
