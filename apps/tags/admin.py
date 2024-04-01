from django.contrib import admin
from .models import (
    Tag,
    TaggedItem,
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag

    list_display = ('title', 'user')
    list_select_related = ['user']

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user = request.user
        if user.is_superuser:
            return qs

        return qs.filter(user=user)


@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    class Meta:
        model = TaggedItem

    list_display = ('tag', 'content_object')
    list_select_related = ['tag']
