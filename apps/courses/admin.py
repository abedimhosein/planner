from admin_searchable_dropdown.filters import AutocompleteFilter
from django.contrib import admin

from .models import (
    Course,
    Part,
)


class SkillFilter(AutocompleteFilter):
    title = 'Skill'  # displayed title
    field_name = 'skill'  # name of the foreign key field


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

    list_display = ('title', 'skill')
    list_editable = ('skill',)
    list_per_page = 10
    search_fields = ('title',)
    list_filter = [SkillFilter]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    class Meta:
        model = Part

    list_display = ('title', 'order')
