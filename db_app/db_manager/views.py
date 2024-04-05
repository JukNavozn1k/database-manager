from django.shortcuts import render

from django.views import View

class Root(View):
    def get(self,request):
        return render(request,'index.html')
# Create your views here.
