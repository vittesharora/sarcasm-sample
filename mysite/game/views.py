from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save() 
			return redirect('/game')
	else:
		form= SignUpForm()

@login_required
def gaming(request):
	if request.user.is_authenticated:
		questions=Question.objects.all()
		return render(request, 'game/home.html', {'questions':questions})
	else:
		return render(request,'game/home.html',{})	
def detail(request, pk):
	question=get_object_or_404(Question, pk=pk)
	return render(request, 'game/detail.html',{'pk':pk,'question':question})

	return render(request, 'game/register.html', {'form':form})				 
def opening(request):
	return render(request, 'game/opening.html',{})