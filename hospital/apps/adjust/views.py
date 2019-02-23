from django.views import View
# Create your views here.
from apps.adjust.models import Adjustprice
from django.shortcuts import render,redirect
from django.db import models


class Addprice(View):
    def get(self,request):
        return render(request,'adjust/adjustprice.html')

    def post(self,request):
        adjustpriceID = request.POST.get("adjustpriceID")
        adjustdrugname = request.POST.get("adjustdrugname")
        adjustpricebefore = request.POST.get("adjustpricebefore")
        adjustpriceafter = request.POST.get("adjustpriceafter")
        drugID = request.POST.get("drugID")

        ad = Adjustprice()
        ad.adjustpriceID=adjustpriceID
        ad.adjustdrugnam=adjustdrugname
        ad.adjustpricebefore=adjustpricebefore
        ad.adjustpriceafter=adjustpriceafter
        ad.drugID=drugID
        ad.save()
        return redirect("/adjust/show")

class Show(View):
    def get(self,request):
        show = Adjustprice.objects.all()
        return render(request,'adjust/showadjustprice.html',{"show":show})

class Updateadjustprice(View):
    def get(self,request):
        adjustpriceID = request.GET.get("adjustpriceID")
        update = Adjustprice.objects.filter(adjustpriceID=adjustpriceID)
        return render(request,'adjust/updateadjustprice.html',{"update":update[0]})
    def post(self,request):
        adjustpriceID = request.POST.get("adjustpriceID")
        adjustdrugname = request.POST.get("adjustdrugname")
        adjustpricebefore = request.POST.get("adjustpricebefore")
        adjustpriceafter = request.POST.get("adjustpriceafter")
        drugID = request.POST.get("drugID")

        adjprice = Adjustprice.objects.get(adjustpriceID=adjustpriceID)

        adjprice.adjustpriceID = adjustpriceID
        adjprice.adjustdrugname = adjustdrugname
        adjprice.adjustpricebefore = adjustpricebefore
        adjprice.adjustpriceafter = adjustpriceafter
        adjprice.drugID = drugID

        adjprice.save()
        return redirect("/adjust/show")

class Delete(View):
    def get(self,request):
        dell = request.GET.get("adjustpriceID")
        Adjustprice.objects.filter(adjustpriceID=dell).delete()
        return redirect("/adjust/show")
