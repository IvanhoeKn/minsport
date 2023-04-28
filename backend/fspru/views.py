from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from .forms import LoginForm
from .models import Users, Events


def index(request):
	# lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = {
	# 	'contests': [{"num": 1, "title": 'Соревнования в Монкипоне'},
	# 				{"num": 2, "title": 'Еще какие-то соревнования'}
	# 				],
	# }
	return render(request, 'fspru/index.html', {"contests": Events.objects.all()[:5]})


def contests(request):
	context = {
		'contests': [{"num": 1, "title": 'Соревнования в Монкипоне'},
					{"num": 2, "title": 'Еще какие-то соревнования'},
					{"num": 3, "title": 'Соревнования в реке'}],
	}
	return render(request, 'fspru/contests.html', context)


def contest_description(request, contest_id):
	context = {
		"title": "Соревнования в Монкипоне",
		"description": """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
	        		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
	        		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
	        		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
	        		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
	        		proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
	        		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
	        		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
	        		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
	        		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
	        		proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
	        		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
	        		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
	        		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
	        		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
	        		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""",
		"date_period": "26.04.2023 - 29.04.2023",
		"city": "Москва",
	}
	return render(request, 'fspru/contest_description.html', context)


def login_index(request):
	if request.method == 'GET':
		form = LoginForm()
		return render(request, 'fspru/login.html', {'form': form})

	elif request.method == 'POST':
		form = LoginForm(request.POST)
		# print("Hello")
		if form.is_valid:
			# print("dwifnwon")
			# print(dir(form.data))
			try:
				# print("=", form.data["login_email"])
				user = Users.objects.get(login_email=form.data["login_email"])
			except:
				# print("except")
				form = LoginForm()
				return render(request, 'fspru/login.html', {'form': form, 'msg': 'Пользователь не найден'})

			if user.password == form.data["password"]:
				request.session['is_auth'] = True
				request.session['user'] = {'id': user.id, 'first_letter': user.second_name[0].upper()}
				return redirect("/")
				# return render(request, 'fspru/index.html')

			else:
				form = LoginForm()
				return render(request, 'fspru/login.html', {'form': form, 'msg': 'Логин или пароль введены неверно'})

		form = LoginForm()
		return render(request, 'fspru/login.html', {'form': form})


def logout(request):
	request.session["is_auth"] = False
	return redirect("/")


def user_contests(requests):
	pass
