# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

from django.utils import timezone


class Utils(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)

	class Meta:
		abstract = True


class Level1(Utils):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name


class Level2(Utils):
	name = models.CharField(max_length=60)
	submenu = models.ForeignKey(Level1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Level3(Utils):
	name = models.CharField(max_length=60)
	newmenu = models.ForeignKey(Level2, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


