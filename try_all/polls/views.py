from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from .models import Question, Choice


def poll_index(request):
    # return HttpResponse("<h1>안녕, 장고야~! views.index다.</h2>")
    context = {
        'latest_question_list': Question.objects.all().order_by('-published_date')
    }
    return render(request, 'polls/poll_index.html', context)


def poll_detail(request, question_id):
    return HttpResponse("It's detail page")
    # try:
    #     selected_title = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    selected_title = get_object_or_404(Question, pk=question_id)
    context = {
        'question': selected_title
    }
    return render(request, 'polls/poll_detail.html', context)


def poll_vote(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     return redirect('poll_index')
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        try:
            choice_pk = request.POST['choice_pk']
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()

        # 선택없이 제출 버튼을 누른경우 'chooice_pk'가 존재하지 않을 때
        except MultiValueDictKeyError:
            context = {
                'question': question,
                'error_message': "다시 선택을 하세요~"
            }
            return render(request, 'polls/poll_detail.html', context)
        # choice가 DB에 아예 없거나  question에 대응하는 것이 없거나
        except Choice.DoesNotExist:
            context = {
                'question': question,
                'error_message': "다시 선택을 하세요~"
            }
            return render(request, 'polls/poll_detail.html', context)
        return redirect('poll_result', question_id=question.pk)
    else:
        return HttpResponse(
            """
            <h1>접근방법이 다릅니다.</h1>
            <a href="/polls/"> 목록으로 </a>
            """,
            status=403
        )


def poll_result(request, question_id):
    return render(
        request,
        "polls/poll_result.html",
        {'question': Question.objects.get(pk=question_id)}
    )

