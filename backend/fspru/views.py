from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from django.http import HttpResponse

from .forms import LoginForm, RegistrationForm
from .models import Users, Events, TableParticipants, Status


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
	return render(request, 'fspru/contests.html', {"contests": Events.objects.all()})


def contest_description(request, contest_id):
	try:
		contest = Events.objects.get(id=contest_id)
	except:
		return redirect("/")

	users_id = TableParticipants.objects.filter(event_id=contest)
	users = [x.user_id for x in users_id]
	# print(users)

	return render(request, 'fspru/contest_description.html', {
		"contest": contest,
		"date_start": contest.data_start.strftime("%d.%m.%Y"),
		"date_end": contest.data_end.strftime("%d.%m.%Y"),
		"users": users,
	})


def login_index(request):
	if request.session.get("is_auth", False):
		return redirect(reverse("fspru:user_contests"))

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
				request.session['user'] = {
					'id': user.id,
					'first_letter': user.second_name[0].upper(),
					"name": f"{user.second_name} {user.first_name[0].upper()}.",
					# "name-role": f"{user.second_name} {user.first_name}: {user.}"
				}
				return redirect("/")

		form = LoginForm()
		return render(request, 'fspru/login.html', {'form': form, 'msg': 'Логин или пароль введены неверно'})

	form = LoginForm()
	return render(request, 'fspru/login.html', {'form': form})


def logout(request):
	request.session["is_auth"] = False
	return redirect("/")


def user_contests(request):
	if request.session.get("is_auth", False):
		contests_id = TableParticipants.objects.filter(user_id=request.session["user"]["id"])
		contests = [con_id.event_id for con_id in contests_id]

		return render(request, "fspru/user_contests.html", {"contests": contests})


def registration_index(request):
	if request.method == 'GET':
		form = RegistrationForm()
		return render(request, 'fspru/signup.html', {'form' : form})

	elif request.method == 'POST':
		# print(request.POST)
		form = RegistrationForm(request.POST)
		if form.is_valid:
			# print(form.data)
			# print(form.data["status"])
			try:
				user = Users.objects.filter(login_email=form.data['login_email'])
				status = Status.objects.get(id=int(form.data["status"]))

			except:
				print("exc")
				form = LoginForm()
				return render(request, 'fspru/signup.html', {'form': form, 'msg': 'Произошла ошибка при регистрации'})

			if len(user) == 0:
				user = Users(
					login_email=form.data["login_email"],
					password=form.data["password"],
					first_name=form.data["first_name"], 
					second_name=form.data["second_name"],
					phone=form.data["phone"],
					status=status,
				)
				user.save()

				request.session['is_auth'] = True
				request.session['user'] = {
					'id': user.id,
					'first_letter': user.second_name[0].upper(),
					"name": f"{user.second_name} {user.first_name[0].upper()}.",
					# "name-role": f"{user.second_name} {user.first_name}: {user.}"
				}

				redirect(reverse("fspru:user_contests"))

			else:
				form = RegistrationForm()
				return render(request, 'fspru/signup.html', {'form' : form, 'msg' : 'Пользователь с такой почтой уже существует'})

	return redirect(reverse("fspru:index"))


def contest_enter(request, contest_id):
	if request.session.get("is_auth", False):
		try:
			contest = Events.objects.get(id=contest_id)
			user = Users.objects.get(id=request.session["user"]["id"])
		except:
			pass

		if len(TableParticipants.objects.filter(user_id=user, event_id=contest)) == 0:
			new_table_participants = TableParticipants(event_id=contest, user_id=user)
			new_table_participants.save()

		return redirect(reverse("fspru:user_contests"))

	return redirect(f"contests/{contest_id}/")


def user_info(request):
	if request.session.get("is_auth", False):
		if request.method == "GET":
			try:
				user = Users.objects.get(id=request.session["user"]["id"])
			except:
				return redirect(reverse("fspru:index"))

			form = RegistrationForm(initial={
				"login_email": user.login_email,
				"first_name": user.first_name,
				"second_name": user.second_name,
				"phone": user.phone,
				"password": user.password,
			})
			# form.data["email"] = user.login_email;

			return render(request, "fspru/user_info.html", {"user": user, "form": form})

		if request.method == "POST":
			print(request.POST.data)

	return redirect(reverse("fspru:index"))
