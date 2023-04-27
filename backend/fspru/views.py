from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
	# lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'contests': ['Соревнования в Монкипоне', 'Еще какие-то соревнования'],
	}
	# тоже самое, что и return HttpResponse(template.render(context, request))
	return render(request, 'fspru/index.html', context)
