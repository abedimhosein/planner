from django.db import models

from utils.funcs import to_jalali_date_time


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def jalali_updated_at(self):
        return to_jalali_date_time(self.updated_at)

    @property
    def jalali_created_at(self):
        return to_jalali_date_time(self.created_at)

    class Meta:
        abstract = True