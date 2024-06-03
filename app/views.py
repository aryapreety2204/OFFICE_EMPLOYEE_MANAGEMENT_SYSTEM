from django.shortcuts import render,HttpResponse
from.models import*
from datetime import datetime
from django.db.models import Q 

# Create your views here.
def index(request):
   return render(request,"index.html")

def View_Employee(request):
  emps = Employee.objects.all()
  context = {
    'emps':emps
  }
  print(context)
  return render(request,"ViewEmployee.Html",context)

 
def Add_Employee(request):
  if request.method=='POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    salary = int(request.POST['salary'])
    bonus = int(request.POST['bonus'])
    phone = int(request.POST['phone'])
    dept = int(request.POST['dept'])
    role = request.POST['role']
    new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
    new_emp.save()
    return HttpResponse("employee added successfully")
  elif request.method=='GET':
    return render(request,"Add_Employee.html") 
  else:  
    return HttpResponse("An Exception Occured! Employer has not been added")
 
def Remove_Employee(request,emp_id=0):
  if emp_id:
    try:
      emp_to_be_removed = Employee.objects.get(id=emp_id)
      emp_to_be_removed.delete()
      return HttpResponse("employee removed Successfully:")
    except:
      return HttpResponse("Please enter a valid Employee Id")
  emps = Employee.objects.all()
  context = {
     'emps':emps
   }
  return render(request,"RemoveEmployee.html",context)
 
def filter_Employee(request):
  if request.method=="POST":
    name = request.POST['name']
    dept = request.POST['dept']
    role = request.POST['role']
    emps = Employee.objects.all()
    if  name:
      emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
    if dept:
      emps = emps.filter(dept__name = dept)
    if role:
      emps = emps.filter(role__name = role)
      
    context = {
      'emps':emps
    }
    return render(request,'ViewEmployee.Html',context)
  elif request.method == "GET":
    return render(request,"FilterEmployee.html")
  else:
    return HttpResponse("Exception occured")
 

   