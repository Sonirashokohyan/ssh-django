from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)    #first colum   max_length means andaza data ka maa limit mekonim
  lastname = models.CharField(max_length=255)     #second colum  har colum dar database banap field yad mesha
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"