# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    hq_passout_year = models.IntegerField()
    hq_degree = models.CharField(max_length=50)
    current_location = models.CharField(max_length=50)
    search_type = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    candidate_desc = models.CharField(max_length=400)
    last_updated = models.DateTimeField()
    class Meta:
        db_table = 'users'

class UsersComments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    user_comment = models.TextField()
    answer = models.TextField()
    is_answered = models.IntegerField(default=0)
    last_updated = models.DateTimeField()
    class Meta:
        db_table = 'users_comments'