from django.shortcuts import render

# Create your views here.
from .forms import AddForm
from .models import Record

def home(request):
	title ='Add/Edit'
	
	#add a form
	form = AddForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"title": title,
		"form" : form
	}

	return render(request,"home.html",context)


def showRecords(request):
	queryset = Record.objects.all()
	context = {
		"object_list" : queryset
	}
	
	return render(request,"base.html",context)
