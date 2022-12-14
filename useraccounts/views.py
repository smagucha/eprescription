from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signupview(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()

	context ={
		'form': form
	}
	return render(request,'useraccounts/signup.html', context)
