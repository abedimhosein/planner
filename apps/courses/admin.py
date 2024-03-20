from django.contrib import admin

from .models import (
    Course,
    Part,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

    list_display = ('title', 'skill')
    list_per_page = 10
    search_fields = ('title',)

    def skill(self, obj: Course):
        return obj.queue.skill.title


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    class Meta:
        model = Part

    list_display = ('title', 'order')
