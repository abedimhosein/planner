from django.contrib.auth.models import User
from django.db import models

from utils.models import BaseModel


class Board(BaseModel):
    title = models.CharField(max_length=255)

    # ------ relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='boards')

    def __str__(self):
        return self.title


class Skill(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    # ------ relations
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='skills')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'board')


class Queue(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    # ------ relations
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='queues')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'board')
