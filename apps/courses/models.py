from django.db import models

from utils.models import AtWhenFields
from apps.skills.models import Skill, Queue


class Course(models.Model, AtWhenFields):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    # ------ relations
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='courses')
    queue = models.ForeignKey(Queue, on_delete=models.PROTECT, related_name='courses')

    def __str__(self):
        return self.title


class CoursePart(models.Model, AtWhenFields):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='parts')

    def __str__(self):
        return self.title


class Note(models.Model, AtWhenFields):
    context = models.TextField()

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='notes')

    @property
    def summary(self):
        return f"{self.context[:15]}..."

    def __str__(self):
        return self.summary


class ProgressLog(models.Model, AtWhenFields):
    context = models.TextField()

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='progress_logs')

    @property
    def summary(self):
        return f"{self.context[:15]}..."

    def __str__(self):
        return self.summary
