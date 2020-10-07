from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from Emploee.forms import EmployeeCreate, EmployeeUpdate
from Emploee.models import Employee



def AddEmploy(request):
    form=EmployeeCreate()
    template_name='create_employ.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=EmployeeCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,template_name,context)

def listEmploy(request):
    template_name='list_employ.html'
    qs=Employee.objects.all()
    context={}
    context["queryset"]=qs
    return render(request,template_name,context)

def EmployeLogin(request):
    form=EmployeeCreate()
    template_name="login.html"
    context={}
    context["form"]=form
    if request.method=='POST':
        username=request.POST.get("User_name")
        # request.session['']


        password=request.POST.get("Password")
        qs=Employee.objects.get(User_name=username)
        # print(qs.employee_id)

        if (qs):
            if (password == qs.Password):
                print("ok")
                print("successfully Login")

                # return redirect("profile")

                context['usr']=qs

                return render(request,'profile.html',context)
            else:
                return render("login.html")
    return render(request, template_name, context)


def Home(request):
    template_name='home.html'
    qs=Employee.objects.all()
    context={}
    context["emp"]=qs
    return render(request,template_name)

#
def Profile(request):
    template_name='profile.html'

    return render(request,template_name)

def UpdateEmploy(request,pk):
    obj=Employee.objects.get(id=pk)
    form=EmployeeUpdate(instance=obj)
    context={}
    context['form']=form
    if request.method=='POST':
        print("ok")
        form=EmployeeUpdate(request.POST,request.FILES)
        if form.is_valid():
            print('ok')
            form.save()
            return redirect('login')
        else:
            context={}
            context['form']=form
            return render(request,'update.html',context)
    return render(request,'update.html',context)
def DeleteEmp(request,pk):
    obj = Employee.objects.get(id=pk)
    if request.method == 'POST':
        print('ok')
        qs =Employee.objects.get(instance=pk).delete()
    return redirect('home')











