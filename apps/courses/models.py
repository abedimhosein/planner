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


class Note(models.Model, AtWhenFields):
    context = models.TextField()

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='notes')


class ProgressLog(models.Model, AtWhenFields):
    context = models.TextField()

    # ------ relations
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='progress_logs')
