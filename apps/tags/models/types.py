from django.utils.translation import gettext_lazy as _

from utils.types import TextChoicesBase


class TagType(TextChoicesBase):
    COURSE = 'COURSE', _('Course')
    NOTE = 'NOTE', _('Note')
    SKILL = 'SKILL', _('Skill')
