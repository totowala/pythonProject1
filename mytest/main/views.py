from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import ToDoList, Item
from . form import CreateNewList

# Create your views here.
def index (response,id):
    ls = ToDoList.objects.get(id=id)
    return render(response,'main\item.html',{"ls": ls})

def home (response):
    if response.method == "POST":
        if response.POST.get("newItem"):
            name = response.POST.get("newItem")
            ls = ToDoList.objects.get(name = name)
            txt = response.POST.get("new" + ls.name)
            if len(txt) >= 2:
                ls.item_set.create(text= txt,complete = False)
                ls.save()
            else:
                print("invalid input")
        else:
            list  = ToDoList.objects.all()
            for ls in list:
                if response.POST.get(ls.name):
                    for item in ls.set_item.all():
                        value = response.POST.get("c" + str(item.id))
                        if response.POST.get("c" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        item.save()
 
    list = ToDoList.objects.all()
    return render(response,'main\home.html',{"list":list})

def form (response):
    form = CreateNewList()
    return render(response,'main\/form.html',{"form":form})

def Create (response):
    if response.method == "POST":
       form = CreateNewList(response.POST)
       if form.is_valid():
           n= form.cleaned_data["name"]
           t = ToDoList(name = n)
           t.save()
           return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()

    return render(response,'main\/form.html',{"form":form})

