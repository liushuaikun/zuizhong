from django.shortcuts import render,redirect
from .models import Suppier
from django.views import View
# Create your views here.


class suppiershow(View) :
    def get(self,request):
        test=Suppier.objects.filter(isdelete=0)
        return render(request,'../templates/suppier/suppiermessage.html',{'test':test})

class addsuppier(View):
    def get(self,request):
        return render(request,'../templates/suppier/suppieradd.html')
    def post(self,request):
        suppierid = request.POST.get('suppierId')
        suppiername = request.POST.get('suppierName')
        suppierphone = request.POST.get('suppierPhone')
        suppieraddress = request.POST.get('suppierAddress')
        suppierman = request.POST.get('suppierMan')
        d=Suppier()
        d.suppierId = suppierid
        d.name = suppiername
        d.phoneNo = suppierphone
        d.address = suppieraddress
        d.linkMan = suppierman
        d.save()
        return redirect("/supplier/suppiershow/")


class updatesuppier(View) :


    def get(self,request):
        suppierid =request.GET.get("suppierId")
        data=Suppier.objects.filter(suppierId=suppierid)
        return render(request,"../templates/suppier/suppierupdate.html",{"data":data[0]})
    def post(self,request):
        supperid=request.POST.get('suppierId')
        suppiername=request.POST.get('suppierName')
        suppierphone=request.POST.get('suppierPhone')
        suppieraddress=request.POST.get('suppierAddress')
        suppierman=request.POST.get('suppierMan')
        d = Suppier.objects.get(suppierId=supperid)
        d.suppierId=supperid
        d.name=suppiername
        d.phoneNo = suppierphone
        d.address = suppieraddress
        d.linkMan = suppierman
        d.save()
        return redirect("/supplier/suppiershow/")


class deletesuppier(View) :
    def get(self,request):
        suppierid = request.GET.get("suppierId")
        data=Suppier.objects.get(suppierId=suppierid)
        data.isdelete="1"
        data.save()
        return redirect("/supplier/suppiershow/")

class quit(View) :
    def get(self,request):
        return render(request,"../templates/head.html")