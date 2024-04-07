from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods

from django.views import View

from . import models
from . import forms

from django.urls import path
'''
   Creates table (CRUD)
'''

class AsyncTable:
    def __init__(self,model,form,tablename) -> None:
        self.model = model
        self.form = form
        self.tablename = tablename

    def gen_urls(self) -> list:
        urls = [path(f'{self.tablename}/table/',self.get_table),
                path(f'{self.tablename}/form/',self.get_form),
                path(f'{self.tablename}/add/',self.add_record),
                path(f'{self.tablename}/delete_modal/<int:id>/',self.get_delete_modal),
                path(f'{self.tablename}/edit_modal/<int:id>/',self.get_edit_modal),
                path(f'{self.tablename}/edit/<int:id>',self.edit_record),
                path(f'{self.tablename}/delete/<int:id>/',self.delete_record),
                path(f'{self.tablename}/search/',self.search_table),]
        return urls
    def get_form(self,request):
        form = self.form()
 
        context = {'form' : form,'tablename':self.tablename}
        return render(request,'form.html',context=context)


    def get_table(self,request):
        objects = self.model.objects.all()

        fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id' and hasattr(field,'verbose_name')]
        fields_verbose = [field.verbose_name for field in self.model._meta.get_fields() if field.name != 'id' and hasattr(field,'verbose_name')]
    
        context = {'fields': fields,'fields_verbose':fields_verbose,'objects':objects,'tablename':self.tablename}
        return render(request,'table.html',context=context)
    
    def get_delete_modal(self,request,id):
        context = {'tablename': self.tablename,'obj_id':id}
        return render(request,'modal_delete.html',context=context)
    
    def get_edit_modal(self,request,id):

        form = self.form(instance=self.model.objects.get(id=id))
        context = {'tablename': self.tablename,'obj_id':id,'form':form}
        return render(request,'modal_edit.html',context=context)
    
    def edit_record(self,request,id):
        form = self.form(request.POST, instance=self.model.objects.get(id=id))
        if form.is_valid():
            form.save()
            return self.get_table(request)
        else: return HttpResponse(f'''
            <div class="alert alert-danger" role="alert">
            <h4 class="alert-heading">Ошибка!</h4>
            <hr>
            <p class="mb-0">{form.errors}</p>
            </div>
            ''')


    def search_table(self,request):
        form = self.form(request.POST)
        cleaned_data = {key : value for key,value in form.data.items() if value != ''}
        objects = self.model.objects.filter(**cleaned_data)

        fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id' and hasattr(field,'verbose_name')]
        fields_verbose = [field.verbose_name for field in self.model._meta.get_fields() if field.name != 'id' and hasattr(field,'verbose_name')]
    
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
        context = {'form':forms.GoodForm()}
        return render(request,'index.html',context=context)

class Manager(View):
    def get(self,request):   
        return render(request,'manager.html')

GoodsTable = AsyncTable(models.Good,forms.GoodForm,'goods')
CategoryTable = AsyncTable(models.Category,forms.CategoryForm,'categories')
CustomerTable = AsyncTable(models.Customer,forms.CustomerForm,'customers')