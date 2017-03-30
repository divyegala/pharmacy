from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=1000)
    age = models.IntegerField()
    loc = models.CharField(max_length=1000)


    def __str__(self):
        return self.name

class Medicines(models.Model):
    name = models.CharField(max_length=1000)
    composition = models.CharField(max_length=1000)
    exp_date = models.DateField()
    manu_date = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()


    def __str__(self):
        return self.name


class Nonmedicine(models.Model):
    name = models.CharField(max_length=1000)
    exp_date = models.DateField()
    manu_date = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=1000)
    qualification = models.CharField(max_length=1000)
    reg_no = models.IntegerField()
    pt_ref = models.IntegerField()

    def __str__(self):
        return self.name

class Location(models.Model):
    loc = models.CharField(max_length=50)
    ip = models.CharField(max_length=15)

    def __str__(self):
        return self.loc
