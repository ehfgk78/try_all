from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Question


def poll_index(request):
    # return HttpResponse("<h1>안녕, 장고야~! views.index다.</h2>")
    context = {
        'latest_question_list' : Question.objects.all().order_by('-published_date')
    }
    return render(request, 'polls/poll_index.html', context)


