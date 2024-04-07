from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods

from django.views import View

from . import models
from . import forms

'''
    Poor code structure
    Very easy to add new endpoints, which can be convenient for asynchronous approach
'''

@require_http_methods(["GET"])
def get_table(request):
    goods = models.Good.objects.all()

    fields = [field.name for field in models.Good._meta.get_fields() if field.name != 'id']
    fields_verbose = [field.verbose_name for field in models.Good._meta.get_fields() if field.name != 'id']
  
    context = {'fields': fields,'fields_verbose':fields_verbose,'goods':goods}
    return render(request,'goods_table.html',context=context)

@require_http_methods(["POST"])
def search_table(request):
    form = forms.GoodForm(request.POST)
    cleaned_data = {key : value for key,value in form.data.items() if value != ''}
    goods = models.Good.objects.filter(**cleaned_data)

    fields = [field.name for field in models.Good._meta.get_fields() if field.name != 'id']
    fields_verbose = [field.verbose_name for field in models.Good._meta.get_fields() if field.name != 'id']
  
    context = {'fields': fields,'fields_verbose':fields_verbose,'goods':goods}
    return render(request,'goods_table.html',context=context)

@require_http_methods(["DELETE"])
def delete_record(request,id):
       good = models.Good.objects.get(id=id)
       good.delete()
       return HttpResponse('')

@require_http_methods(["POST"])
def add_record(request):
        good = forms.GoodForm(request.POST)
        if good.is_valid():
            good.save()
            return get_table(request)
        else: return HttpResponse(f'''
        <div class="alert alert-danger" role="alert">
        <h4 class="alert-heading">Ошибка!</h4>
        <hr>
        <p class="mb-0">{good.errors}</p>
        </div>
        ''')


'''
    Sync handlers
    Good code structure.
    Less flexible to changes
'''
class Home(View):
    def get(self,request):   
        return render(request,'index.html')

class GoodsManager(View):
    def get(self,request):   
        good_form = forms.GoodForm()
        context = {'good_form':good_form}
        return render(request,'goods_manager.html',context=context)
