from django.shortcuts import render,redirect
from .models import Account2,Transaction,Card,Budget
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from stdnum import luhn
from datetime import datetime

# Create your views here.
def main(request):
    return render(request,'Main/main1.html')


@login_required(login_url='login')
def transection(request):
    if request.method == "POST":
        title = request.POST.get("title")
        amount = request.POST.get("amount")
        transaction_type = request.POST.get("transaction_type")
        category = request.POST.get("category")
        date = request.POST.get("date")
        notes = request.POST.get("notes")
        print(title,amount,transaction_type,category,date,notes)
        print(request.user.is_authenticated)
        if title and amount and transaction_type and category and date :
            acc = Account2.objects.get(user=request.user)
            Transaction.objects.create(
                  account=acc,
                  title=title,
                  transaction_type=transaction_type,
                  category=category,
                  amount=amount,
                  date=date,
                  notes=notes
             )
            acc.used_credit=int(amount)
            acc.balance=acc.balance-int(amount)
            acc.save()
            return redirect('card') 
          

    return render(request,"Main/transection.html")



@login_required(login_url='login')
def dash(request):
    info = Account2.objects.get(user=request.user)
    
    used = info.used_credit

    balance=info.balance
    percent = (used/balance)*100

    

    return render(request,'Main/dash.html',{'info':info,"used":used,'balance':balance,'percent':percent})

@login_required(login_url='login')
def form_(request):
    if request.method =="POST":
        user = request.user
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        account_type =request.POST.get("Account_Type")
        balance = request.POST.get("amount")
        card_no = request.POST.get("card_number")
        Cvv=  request.POST.get("cvv")
        context ={
            'fieldValues':request.POST
        }
        if luhn.is_valid(str(card_no)):
            if first_name and last_name and account_type and balance and card_no and Cvv:
                if len(str(card_no)) == 16 and len(str(Cvv))==3:
                    Account2.objects.create(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    account_type=account_type,
                    balance=balance,
                    card_no=card_no,
                    Cvv=Cvv
                    )
                    
                    return redirect("dash")
                else:

                    return render(request,"Main/form.html",context)
            else:
                return render(request,"Main/form.html",context)
        else:
                return render(request,"Main/form.html",context)
    
    return render(request,'Main/form.html')
    
@login_required(login_url="login")
def list_(request):
    acc = Account2.objects.get(user=request.user)
    trans= Transaction.objects.filter(account=acc)


    return render(request,"Main/list.html",{'trans':trans})
@login_required(login_url="login")
def card(request):
    acc = Account2.objects.get(user=request.user)
    if request.method=="POST":
        cardholder_name = request.POST.get("cardholder_name")
        card_number = request.POST.get("card_number")
        recieve_no = request.POST.get("recieve_no")
        expiry_month = request.POST.get("expiry_month")
        expiry_year = request.POST.get("expiry_year")
        cvv = request.POST.get("cvv")

        if cardholder_name and card_number and recieve_no and expiry_month and expiry_year and cvv:
             Card.objects.create(
                  acc=acc,
                  cardholder_name=cardholder_name,
                  card_number=card_number,
                  reciever_no=recieve_no,
                  expiry_month=expiry_month,
                  expiry_year=expiry_year,
                  cvv=cvv
             )
             return redirect('cmlt_transection')
        else:
             return redirect('card')
     
    return render(request,"Main/card.html")


@login_required(login_url="login")
def transection_complete(request):
     return render(request,'Main/complete_transection.html')

def budget(request):
    if request.method =="POST":
        category = request.POST.get("category")
        income = request.POST.get("income")
        expenses = request.POST.get("expenses")
        notes = request.POST.get("notes")
        if category and income and expenses :
            Budget.objects.create(
                user = request.user,
                category= category,
                mounthly_in=income,
                limit= expenses
            )

            return redirect('mybudget')
        else:
            return redirect('budget')

    return render(request,'Main/budget.html')


def mybudget(request):
    budget=Budget.objects.filter(user = request.user)
    for b in budget:
        u = model_to_dict(b)
        used= u['total']
        bg= u['limit']
        percent=(used/bg)*100

    if budget.exists():
        return render(request,'Main/mybudget.html',{'budget':budget,'used':used,'percent':percent})
    

    return render(request,'Main/mybudget.html')
    

