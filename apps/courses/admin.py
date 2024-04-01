from admin_searchable_dropdown.filters import AutocompleteFilterFactory
from django.contrib import admin

from .models import (
    Course,
    Part,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

    list_display = ('title', 'skill', 'duration')
    search_fields = ('title',)
    list_filter = [
        AutocompleteFilterFactory('Skill', 'skill')
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user = request.user
        if user.is_superuser:
            return qs

        return qs.filter(skill__board__user=user)


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    class Meta:
        model = Part

    list_display = ('title', 'order')

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user = request.user
        if user.is_superuser:
            return qs

        return qs.filter(course__skill__board__user=user)
