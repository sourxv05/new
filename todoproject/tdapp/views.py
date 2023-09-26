from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import todoforms
from .models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklist(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 't2'

class detailview(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name = 't3'

class updateview(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 't4'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detview',kwargs={'pk':self.object.id})


class deletelist(DeleteView):
    model = task
    template_name = 'delete.html'
    def get_success_url(self):
        return reverse_lazy('genlist')



def index(request):
    t2=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        t1=task(name=name,priority=priority,date=date)
        t1.save()
    return render(request,'index.html',{'t2':t2})

def delete(request,taskid):
    t3=task.objects.get(id=taskid)
    if request.method=='POST':
        t3.delete()
        return redirect('/')
    return render(request,'delete.html')
def edit(request,id):
    t=task.objects.get(id=id)
    form=todoforms(request.POST or None , instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':t})


