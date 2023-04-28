from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
	# lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'contests': [{"num": 1, "title": 'Соревнования в Монкипоне'},
					{"num": 2, "title": 'Еще какие-то соревнования'}
					],
	}
	return render(request, 'fspru/index.html', context)


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
