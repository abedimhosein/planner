from django.contrib import admin
from .models import Tag, TaggedItem


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag

    list_display = ('title',)


@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    class Meta:
        model = TaggedItem

    list_display = ('tag', 'content_object')
