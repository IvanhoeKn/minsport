from django.shortcuts import render
from .forms import LoginForm

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


def login_index(request):
	if request.method == 'GET':
		form = LoginForm()
		return render(request, 'fspru/login.html', {'form': form})

	elif request.method == 'POST':
		form = LoginForm(request.POST)
		# master = get_object_or_404(Portfolio, pk = master_id)
	# response_data = dict()

	# if request.method == 'POST':
	# 	form = ReviewForm(request.POST)

	# 	if form.is_valid:
	# 		master.review_set.create(
	# 				name = form.data['name'],
	# 				surname = form.data['surname'],
	# 				description = form.data['description'],
	# 				pub_date = timezone.localtime(timezone.now()),
	# 			)

	# 		last_review = master.review_set.latest('pub_date')
	# 		response_data['description'] = last_review.description
	# 		response_data['full_name'] = last_review.get_full_name()
	# 		response_data['pub_date'] =	last_review.get_pub_date()

	# 		return JsonResponse(response_data)

	# return HttpResponseRedirect(reverse('smremonts:reviews', args = {master_id,}))
	# return render(request, 'fspru/login.html')


	# master = get_object_or_404(Portfolio, pk = master_id)
	# form = ReviewForm()
	# page = request.GET.get('page', 1)

	# review_list = master.review_set.order_by('-pub_date')
	# paginator = Paginator(review_list, settings.REVIEWS_PAGE_PAGINATION_BY)
	# try:
	# 	review_list = paginator.page(page)
	# except PageNotAnInteger:
	# 	review_list = paginator.page(1)
	# except EmptyPage:
	# 	review_list = paginator.page(paginator.num_pages)

	# context = {
	# 	'form': form,
	# 	'review_list': review_list,
	# 	'master': master,
	# }

	# return render(request, 'smremonts/review.html', context)