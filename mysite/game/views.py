from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def gaming(request):
	questions=Question.objects.all()
	return render(request, 'game/home.html', {'questions':questions})
def detail(request, pk):
	question=get_object_or_404(Question, pk=pk)
	return render(request, 'game/detail.html',{'pk':pk,'question':question})
def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save() 
			return redirect('/game')
	else:
		form= SignUpForm()

	return render(request, 'game/register.html', {'form':form})				 
def opening(request):
	return render(request, 'game/opening.html',{})