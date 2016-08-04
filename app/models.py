"""
Definition of models.
"""



 #This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:                    #   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True                  #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class PostTb01(models.Model):
    id = models.IntegerField()  # AutoField?
    post_id = models.TextField(primary_key=True)  # This field type is a guess.
    site_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    heading = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    full_story = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)  # This field type is a guess.
    post_date = models.DateTimeField(blank=True, null=True)
    img_src = models.TextField(blank=True, null=True)
    post_link = models.TextField(blank=True, null=True)
    scrap_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_tb_01'