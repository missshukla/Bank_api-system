from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_id=models.AutoField(primary_key=True)
    bank_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    branch=models.CharField(max_length=50)
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField()
    def __str__(self):
        return self.bank_name+" "+self.address+" "+self.branch

class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=(('manager','manager'),
                                                 ('cashier','cashier'),
                                                 ('clerk','clerk')))
    def __str__(self):
        return self.name+" "+self.type+" "+self.address
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE)

