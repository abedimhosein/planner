from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.exceptions import InvalidInputError


class ChoicesBase:
    _value2member_map_ = None
    _value2label_map_ = None

    @classmethod
    def to_obj(cls, value):
        if isinstance(value, cls):
            return value

        value = value.strip().upper()
        try:
            return cls._value2member_map_[value]
        except KeyError:
            raise InvalidInputError(f'Invalid {cls.__name__} value ---> ({value})')

    @classmethod
    def to_fa(cls, value):
        value = cls.to_obj(value)
        return cls._value2label_map_[value]

    @classmethod
    def serialize(cls, value):
        value = cls.to_obj(value)
        return {
            'value': value.value,
            'label': value.label,
        }

    @staticmethod
    def to_contentType(value):
        raise NotImplementedError("must be implemented in subclass")


class TextChoicesBase(ChoicesBase, models.TextChoices):
    pass
