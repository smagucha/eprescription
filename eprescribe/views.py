from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import PrescribeForm
from .models import PrescribeMed

@login_required(login_url='/accounts/login/')
def home(request):
	prescription = PrescribeMed.objects.all()
	context = {'prescription': prescription}
	return render(request, 'eprescribe/home.html', context)


@login_required(login_url='/accounts/login/')
def createprescribe(request):
	
	if request.method == 'POST':
		form = PrescribeForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = PrescribeForm()

	context ={'form': form, 'title':'med form'}
	return render(request, 'eprescribe/createform.html', context)


@login_required(login_url='/accounts/login/')
def updateprescribe(request, id):

	updatemed = PrescribeMed.objects.get(id = id)
	if request.method =='POST':
		form = PrescribeForm(request.POST or None, instance = updatemed)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = PrescribeForm(instance = updatemed)

	context ={'form': form, 'title':'med form'}
	return render(request, 'eprescribe/createform.html', context)


@login_required(login_url='/accounts/login/')
def deletemed(request, id):

	updatemed = PrescribeMed.objects.get(id = id)
	if request.method =='POST':
		updatemed.delete()
		return redirect('home')
	context ={'updatemed': updatemed, 'title':'med form'}
	return render(request, 'eprescribe/delete.html', context)



def detailmed(request, id):
	updatemed = PrescribeMed.objects.get(id = id)
	context ={'updatemed': updatemed, 'title':'med form'}
	return render(request, 'eprescribe/detail.html', context)