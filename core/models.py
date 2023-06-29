import enum
import uuid
from decimal import Decimal

from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone

# from .managers import BaseSuperManager


class BaseSuperModel(models.Model):
    # id = models.UUIDField(
    # verbose_name="Indentificador",
    # primary_key=True,
    # default=uuid.uuid4,
    # editable=False,
    # )
    created_at = models.DateTimeField(
        verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Atualizado às", auto_now=True)
    # deleted_at = models.DateTimeField(
    # verbose_name="Deletado às", blank=True, null=True, default=None
    # )
    # for logical delete
    # deleted = models.BooleanField(verbose_name="Deletado", default=False, db_index=True)
    # managers
    # objects = BaseSuperManager()
    # objects_all = models.Manager()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    # def delete(self, force=False):
     #   if force:
      #      return super().delete()

        #self.deleted = True
        #self.deleted_at = timezone.now()
        # self.save()
