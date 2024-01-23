from django.contrib import admin
from .models import Course, Note, ProgressLog


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

    list_display = ('title',)


admin.register(Note)
admin.register(ProgressLog)
