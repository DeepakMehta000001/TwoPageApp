from django.shortcuts import render


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
from .forms import AddForm
from .models import Record

def add(request):
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
	queryset_list = Record.objects.all()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list" : queryset
	}
	
	return render(request,"base.html",context)




