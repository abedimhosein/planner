from django.db import models

from apps.skills.models import Queue
from utils.models import BaseModel


class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    # ------ relations
    queue = models.ForeignKey(Queue, on_delete=models.PROTECT, related_name='courses')

    def __str__(self) -> str:
        return self.title


class Part(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    level = models.PositiveIntegerField(default=0)

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='parts')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        unique_together = ('order', 'course')
