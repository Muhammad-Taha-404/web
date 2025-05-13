from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)  
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    used_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  
    card_no = models.BigIntegerField()  
    Cvv = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Account2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)  
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    used_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  
    card_no = models.BigIntegerField()  
    Cvv = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class Transaction(models.Model):
    account = models.ForeignKey(Account2, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])
    category = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)


class Card(models.Model):
    acc = models.ForeignKey(Account2, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=200)
    card_number = models.BigIntegerField()  
    expiry_month = models.IntegerField()
    expiry_year= models.IntegerField()
    cvv = models.IntegerField()
    reciever_no = models.BigIntegerField() 

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    mounthly_in =models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField(auto_now_add=True)
    total = models.IntegerField(default=0)


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deadline = models.DateField()

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=100)  # e.g. stock, crypto
    name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    current_value = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateField()











