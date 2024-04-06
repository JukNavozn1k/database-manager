from django.shortcuts import render,HttpResponse

from django.views import View

from . import models
from . import forms

class GoodsTable(View):
    def get(self,request):
       goods = models.Good.objects.all()
       fields = [field.verbose_name for field in models.Good._meta.get_fields() if field.name != 'id']
    
       print(request.GET) 
       context = {'fields':fields,'goods':goods}
       return render(request,'goods_table.html',context=context)
    def delete(self,request,id):
       good = models.Good.objects.get(id=id)
       good.delete()
       return HttpResponse('')
    def post(self,request):
       good = forms.GoodForm(request.POST)
       if good.is_valid():
            good.save()
            return self.get(request)
       else: return HttpResponse(f'''
<div class="alert alert-danger" role="alert">
  <h4 class="alert-heading">Ошибка!</h4>
  <hr>
  <p class="mb-0">{good.errors}</p>
</div>
''')


class Home(View):
    def get(self,request):   
        return render(request,'index.html')

class GoodsManager(View):
    def get(self,request):   
        good_form = forms.GoodForm()
        context = {'good_form':good_form}
        return render(request,'goods_manager.html',context=context)
# Create your views here.
