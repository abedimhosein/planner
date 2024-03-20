from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utils.models import BaseModel


class Folder(BaseModel):
    title = models.CharField(max_length=255)
    level = models.PositiveIntegerField(default=0)

    # ------ relations
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True
    )

    def __str__(self):
        return self.title


class Note(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    context = models.TextField()

    # ------ limits
    limit = (
            models.Q(app_label='apps.courses', model='Course') |
            models.Q(app_label='apps.courses', model='Part')
    )

    # ------ relations
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True)

    object_id = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()

    @property
    def summary(self) -> str:
        return f"{self.context[:15]}..."

    def __str__(self) -> str:
        return self.title or self.summary

    class Meta:
        ordering = ('-created_at',)
