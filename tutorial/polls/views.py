from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, Choice, Comment, Voted


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.all()


class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Question
    template_name = 'polls/create.html'
    fields = ['question_text']

    def post(self, request):
        print(request.POST)
        req = request.POST
        var = Question(user=request.user, question_text=req['question'],
                       date_pub=timezone.now())
        var.save()

        c1 = Choice(question=var, choice_text=req['c1'], votes=0)
        c2 = Choice(question=var, choice_text=req['c2'], votes=0)
        c3 = Choice(question=var, choice_text=req['c3'], votes=0)
        c1.save()
        c2.save()
        c3.save()

        return HttpResponseRedirect(reverse('polls:index'))


class CommentView(LoginRequiredMixin, generic.edit.CreateView):
    model = Comment

    def post(self, request):
        print(request.POST)
        req = request.POST
        question = get_object_or_404(Question, pk=req['question'])
        comment = Comment(user=request.user, question=question,
                          comment_text=req['comment'])

        comment.save()
        return redirect('/polls/' + req['question'])


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        voted = Voted(user=request.user, question=question)
        voted.save()
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id, )))
