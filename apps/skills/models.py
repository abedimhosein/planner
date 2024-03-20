from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from utils.models import BaseModel


class Board(BaseModel):
    title = models.CharField(max_length=255)

    # ------ relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='boards')

    def __str__(self):
        return self.title


class Skill(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)
    level = models.PositiveIntegerField(default=0)

    # ------ relations
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='skills')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [('title', 'board'), ]

    def save(self, *args, **kwargs):
        if self.parent and self.board != self.parent.board:
            raise ValidationError("Boards must be the same.")

        return super().save(*args, **kwargs)


class Queue(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    # ------ relations
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='queues')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [('title', 'skill'), ]
