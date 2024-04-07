from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods

from django.views import View

from . import models
from . import forms

'''
    Poor code structure
    Very easy to add new endpoints, which can be convenient for asynchronous approach
'''

class AsyncTable:
    def __init__(self,model,form,tablename) -> None:
        self.model = model
        self.form = form
        self.tablename = tablename
        pass
   
    def get_form(self,request):
        form = self.form()
 
        context = {'form' : form,'tablename':self.tablename}
        return render(request,'form.html',context=context)


    def get_table(self,request):
        objects = self.model.objects.all()

        fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id']
        fields_verbose = [field.verbose_name for field in self.model._meta.get_fields() if field.name != 'id']

        context = {'fields': fields,'fields_verbose':fields_verbose,'objects':objects,'tablename':self.tablename}
        return render(request,'table.html',context=context)

    def search_table(self,request):
        form = self.form(request.POST)
        cleaned_data = {key : value for key,value in form.data.items() if value != ''}
        objects = self.model.objects.filter(**cleaned_data)

        fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id']
        fields_verbose = [field.verbose_name for field in self.model._meta.get_fields() if field.name != 'id']
    
        context = {'fields': fields,'fields_verbose':fields_verbose,'objects':objects,'tablename':self.tablename}
        return render(request,'table.html',context=context)

    
    def delete_record(self,request,id):
        object = self.model.objects.get(id=id)
        object.delete()
        return HttpResponse('')


    def add_record(self,request):
            object_form = self.form(request.POST)
            if object_form.is_valid():
                object_form.save()
                return self.get_table(request)
            else: return HttpResponse(f'''
            <div class="alert alert-danger" role="alert">
            <h4 class="alert-heading">Ошибка!</h4>
            <hr>
            <p class="mb-0">{object_form.errors}</p>
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
       
        return render(request,'manager.html')

GoodsTable = AsyncTable(models.Good,forms.GoodForm,'goods')