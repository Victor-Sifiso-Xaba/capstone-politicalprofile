from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, "polls/poll.html", context)
    else:
        messages.info(request, "You need to log in to view polls.")
        return HttpResponseRedirect(reverse('user_auth:login_user'))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def vote(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        selected_choices_ids = request.POST.getlist('choice')

        if len(selected_choices_ids) > 3:
            # If the user selects more than three choices, display an error message
            messages.error(request, "You can select at most three choices.")
            return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

        try:
            for choice_id in selected_choices_ids:
                selected_choice = question.choice_set.get(pk=choice_id)
                selected_choice.votes += 1
                selected_choice.save()
        except (KeyError, Choice.DoesNotExist):
            # If a choice does not exist, display an error message
            messages.error(request, "Invalid choice.")
            return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
        else:
            messages.success(request, "Your vote was recorded successfully.")
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        # If the request method is not POST, redirect to the detail page
        return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))
