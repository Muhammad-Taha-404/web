from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main1"),
    path('dash/',views.dash,name="dash"),
    path('form/',views.form_,name="form"),
    path('transection/',views.transection,name='transection'),
    path('transection_complete/',views.transection_complete,name='cmlt_transection'),
    path('transection_list/',views.list_,name='list'),
    path('Card/',views.card,name='card'),
    path('budget/',views.budget,name='budget'),
    path('mybudget/',views.mybudget,name='mybudget'),

    
]