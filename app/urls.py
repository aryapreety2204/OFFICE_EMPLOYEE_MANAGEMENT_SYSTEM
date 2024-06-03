from django.urls import path,include
from . views import*

urlpatterns = [
   path("",index),
   path("all_employee/",View_Employee,name="View_Employee"),
   path("add_employee/",Add_Employee ,name="Add_Employee"),
   path("remove_employee/",Remove_Employee,name="Remove_Employee"),
   path("remove_employee/<int:emp_id>/",Remove_Employee,name="Remove_Employee"),
   path("filter_employee/",filter_Employee, name="filter_Employee")
   
    
]