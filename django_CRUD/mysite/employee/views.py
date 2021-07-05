from django.shortcuts import render
from . models import tbl_emp
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
def home(request):
	context = {
	'employees' : tbl_emp.objects.all()
	}
	return render(request, "employee/home.html", context)

def details(request, emp_id):
	return render(request, 'employee/details.html', {
		'employee' : tbl_emp.objects.get(pk=emp_id)
		})

class tbl_empCreateView(CreateView):
    model = tbl_emp
    template_name = 'employee/newEmp.html'
    fields = '__all__'

class tbl_empUpdateView(UpdateView):
    model = tbl_emp
    fields = '__all__'
    template_name = 'employee/updateEmp.html'



class tbl_empDeleteView(DeleteView):
    model = tbl_emp
    success_url = '/'
    template_name = 'employee/deleteEmp.html'
