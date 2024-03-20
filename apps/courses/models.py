from django.db import models

from utils.models import BaseModel
from apps.skills.models import Skill, Queue


class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    # ------ relations
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='courses')
    queue = models.ForeignKey(Queue, on_delete=models.PROTECT, related_name='courses')

    def __str__(self) -> str:
        return self.title


class Part(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

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


class Note(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    context = models.TextField()

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='notes')

    @property
    def summary(self) -> str:
        return f"{self.context[:15]}..."

    def __str__(self) -> str:
        return self.title or self.summary

    class Meta:
        ordering = ('-created_at',)



