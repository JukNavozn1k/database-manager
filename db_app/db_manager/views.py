from django.shortcuts import render

from django.views import View

from . import models
from . import forms

class Home(View):
    def get(self,request):
        goods = models.Good.objects.all()
        good_form = forms.GoodForm()
        context = {'goods':goods,'good_form':good_form}

        return render(request,'index.html',context=context)
# Create your views here.
