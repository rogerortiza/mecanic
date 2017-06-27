from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm

def landingPage(request):
	if request.user.is_authenticated():
		return redirect("home")

	message_login = None
	message_register = None
	form_register = RegisterForm()
	form_login = LoginForm()

	if request.method == "POST":
		if "email" in request.POST:
			form_register = RegisterForm(request.POST or None)
			if form_register.is_valid():
				new_user = form_register.save(commit = False)
				new_user_password = new_user.password
				new_user.set_password(new_user.password)
				new_user.save()

				user = authenticate(username = new_user.username, password = new_user_password)

				if user is not None:
					login_django(request, user)
					return redirect("home")
			else:
				message_register = "No se pudo crear el usuario"
		else:
			usernamePost = request.POST["username"]
			passwordPost = request.POST["password"]

			user = authenticate(username=usernamePost, password=passwordPost)

			if user is not None:
				login_django(request, user)
				return redirect("home")
			else:
				message_login = "Username o password incorrectos"


	context = {
		'form_login' : form_login,
		'form_register' : form_register,
		'message_login' : message_login,
		'message_register' : message_register
	}
	return render(request, 'index.html', context)

@login_required(login_url = "landing_page")
def home(request):
	return render(request, 'dashboard/home.html', {})

@login_required(login_url = "landing_page")
def logout(request):
	logout_django(request)
	return redirect("landing_page")