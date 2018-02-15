# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime as dt

# Create your models here.

class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    authority = models.TextField()

class Data_analyzer(models.Model):
    created_user_id = models.IntegerField()
    description = models.TextField(blank = True)
    num_text_field = models.IntegerField(default = 0)
    num_int_field = models.IntegerField(default = 0)


class User_accessibility(models.Model):
    data_analyzer_id = models.ForeignKey('Data_analyzer', on_delete = models.CASCADE)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    

class Data_record(models.Model):
    data_analyzer_id = models.ForeignKey('Data_analyzer', on_delete = models.CASCADE)
    record_creation_time = models.DateTimeField(default = dt.now, blank = True)
    F1 = models.FloatField(blank = True)
    F2 = models.FloatField(blank = True)
    F3 = models.FloatField(blank = True)
    F4 = models.FloatField(blank = True)
    F5 = models.FloatField(blank = True)
    F6 = models.FloatField(blank = True)
    F7 = models.FloatField(blank = True)
    F8 = models.FloatField(blank = True)
    F9 = models.FloatField(blank = True)
    F10 = models.FloatField(blank = True)
    F11 = models.FloatField(blank = True)
    F12 = models.FloatField(blank = True)
    F13 = models.FloatField(blank = True)
    F14 = models.FloatField(blank = True)
    F15 = models.FloatField(blank = True)
    F16 = models.FloatField(blank = True)
    F17 = models.FloatField(blank = True)
    F18 = models.FloatField(blank = True)
    F19 = models.FloatField(blank = True)
    F20 = models.FloatField(blank = True)
    F21 = models.TextField(blank = True)
    F22 = models.TextField(blank = True)
    F23 = models.TextField(blank = True)
    F24 = models.TextField(blank = True)
    F25 = models.TextField(blank = True)
    F26 = models.TextField(blank = True)
    F27 = models.TextField(blank = True)
    F28 = models.TextField(blank = True)
    F29 = models.TextField(blank = True)
    F30 = models.TextField(blank = True)


class Data_record_attribute_hash(models.Model):
    data_analyzer_id = models.ForeignKey('Data_analyzer', on_delete = models.CASCADE)
    index = models.TextField()
    actu_name = models.TextField()

class Detection_algorithm(models.Model):
    data_analyzer_id = models.ForeignKey('Data_analyzer', on_delete = models.CASCADE)
    attribute_index = models.TextField()
    algorithm_path = models.TextField()
    algorithm_description = models.TextField(blank = True)


class Anomaly_record(models.Model):
    data_record_id = models.ForeignKey('Data_record', on_delete = models.CASCADE)
    attribute_index = models.TextField()
    record_time = models.DateTimeField()
    int_value = models.FloatField(blank = True)
    text_field = models.TextField(blank = True)

class Anomaly_classifier(models.Model):
    data_record_id = models.ForeignKey('Data_record', on_delete = models.CASCADE)
    path = models.TextField()
    classifier_type = models.TextField(blank = True)
    threshold = models.FloatField(blank = True)
    configuration_dict = models.TextField(blank = True)
    description = models.TextField(blank = True)

