from django.shortcuts import render,HttpResponse

from django.views import View

from . import models
from . import forms

class GoodsTable(View):
    def get(self,request):
       goods = models.Good.objects.all()
       context = {'goods':goods}
       return render(request,'goods_table.html',context=context)


class GoodsManager(View):
    def get(self,request):
        
        good_form = forms.GoodForm()
        context = {'good_form':good_form}
       

        return render(request,'index.html',context=context)
# Create your views here.
