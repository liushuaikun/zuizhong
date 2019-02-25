from django.shortcuts import render,redirect
from .models import drugsuppier
from django.views import View


# Create your views here.


class contractshow(View) :
    def get(self,request):
        test=drugsuppier.objects.filter(isdelete=0)
        return render(request,"../templates/contract/contractshow.html",{"test":test})

class contractadd(View) :
    def get(self,request):
        return render(request,"../templates/contract/contractadd.html")
    def post(self,request):
        suppierId = request.POST.get('suppierId')
        drupId = request.POST.get('drupId')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        userId = request.POST.get('userId')
        time = request.POST.get('time')
        d = drugsuppier()
        d.suppierId = suppierId
        d.drugId = drupId
        d.price = price
        d.amount = amount
        d.userId = userId
        d.time = time
        d.save()
        return redirect("/contract/contractshow")


class contractupdate(View) :
    def get(self,request):
        contractid=request.GET.get('suppierId')
        data=drugsuppier.objects.filter(suppierId=contractid)
        return render(request,"../templates/contract/contractupdate.html",{'data':data[0]})

    def post(self,request):
        suppierId=request.POST.get('suppierId')
        drupId=request.POST.get('drupId')
        price=request.POST.get('price')
        amount=request.POST.get('amount')
        userId=request.POST.get('userId')
        time=request.POST.get('time')
        d=drugsuppier.objects.get(suppierId=suppierId)
        d.suppierId=suppierId
        d.drugId=drupId
        d.price=price
        d.amount=amount
        d.userId=userId
        d.time=time
        d.save()
        return  redirect("/contract/contractshow")

class contractdelete(View) :
    def get(self,request):
        suppierid = request.GET.get("suppierId")
        data=drugsuppier.objects.get(suppierId=suppierid)
        data.isdelete="1"
        data.save()
        return redirect("/contract/contractshow")


class quit(View) :
    def get(self, request):
        return render(request, "../templates/head.html")