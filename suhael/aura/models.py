from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
 Bln=models.CharField(max_length=20,primary_key="Bln")
 name=models.CharField(max_length=100)
 LoanAmount=models.IntegerField()
 Adress=models.CharField(max_length=300)
 age=models.IntegerField()
 phoneNO=models.IntegerField()

class BankLoanAdmin(admin.ModelAdmin):
 list_display=('Bln','name','LoanAmount','Adress','age','phoneNO')
