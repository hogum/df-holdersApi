# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import uuid


class Meal(models.Model):

    name = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_id = models.CharField(max_length=255, blank=True)
    ordered_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.receipt_id:
            self.receipt_id = self.create_meal_receipt()

        super(Meal, self).save(*args, **kwargs)

    def __repr__(self):
        return "{} - {}".format(self.name, self.receipt_id)

    @classmethod
    def create_meal_receipt(cls):
        return str(uuid.uuid4()).split('-')[-1]

    class Meta:
        ordering = ["-ordered_at"]


class DishType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
