from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utils.models import BaseModel
from .types import TagType


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    # ------ relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tags')


class TaggedItem(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='items')
    type = models.CharField(max_length=6, choices=TagType.choices, editable=False)

    limit = (
            models.Q(app_label='courses', model='Note') |
            models.Q(app_label='courses', model='Course') |
            models.Q(app_label='skills', model='Skill')
    )

    # ------ relations
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    content_object = GenericForeignKey()

    def save(self, *args, **kwargs) -> None:
        self.type = TagType.to_obj(self.content_type.model)

        return super().save(*args, **kwargs)
