from django.shortcuts import render,redirect
from CRUD.models import CustomerModel
from django.contrib import messages
from CRUD.forms import *
from django.contrib import auth



def showcustomer(request):
    showAll = CustomerModel.objects.all()
    return render(request,'index.html',{"data":showAll})


def registercustomer(request):
    if request.method == "POST":
        if request.POST.get('customername') and request.POST.get('customerphone') and request.POST.get('customeraddress') and request.POST.get('customeremail') and request.POST.get('customerpassword') :
            saveRecord =  CustomerModel()
            saveRecord.customername = request.POST.get('customername')
            saveRecord.customerphone = request.POST.get('customerphone')
            saveRecord.customeraddress = request.POST.get('customeraddress')
            saveRecord.customeremail = request.POST.get('customeremail')
            saveRecord.customerpassword = request.POST.get('customerpassword')
            saveRecord.save()
            messages.success(request,'Customer '+saveRecord.customername+ ' is saved Successfully..!')
            return render(request,'register.html')
    else:
        return render(request,'register.html')


def updatecustomer(request,id):
    updateObj = CustomerModel.objects.get(id = id)
    return render(request,'update.html',{"CustomerModel":updateObj})


def updateRecord(request,id):
    updateCust = CustomerModel.objects.get(id=id)
    form = CustomerForms(request.POST,instance=updateCust)

    if form.is_valid():
        form.save()
        messages.success(request,'Record updated Successfully')
        return render(request,'update.html',{"CustomerModel":updateCust})


def deletecustomer(request,id):
    deleteCust  = CustomerModel.objects.get(id=id)
    deleteCust.delete()
    showData = CustomerModel.objects.all()
    return render(request,"index.html",{"data":showData})


def logincustomer(request):
    if request.method == "POST":
        customeremail = request.POST['customeremail']
        customerpassword = request.POST['customerpassword']

        user = auth.authenticate(username=customeremail,password=customerpassword)
        if user is None:
            return redirect('logincustomer')
        else:
            return redirect('showcustomer')
    else:
        return render(request,'login.html')
    
    
