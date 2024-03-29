from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utils.models import BaseModel


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    # ------ relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='tags')

    class Meta:
        unique_together = ('title', 'user')


class TaggedItem(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='items')

    # ------ limits
    limit = (
            models.Q(app_label='apps.notes', model='Note') |
            models.Q(app_label='apps.courses', model='Course') |
            models.Q(app_label='apps.skills', model='Skill')
    )

    # ------ generic relations
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    content_object = GenericForeignKey()
