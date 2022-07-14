from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question, Choice
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
def index(request):
    q = Question.objects.all()[:5]
    return render(request,'polls/index.html',{"question_list":q})

class DetailView(DetailView):
    model = Question

class ResultsView(DetailView):
    model = Question

    template_name = 'polls/results.html'
    

def vote(request,qid):
    q = get_object_or_404(Question, pk=qid)
    try:
        choice_pk = q.choice_set.get(pk=request.POST['selected'])
        print(choice_pk)
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/question_detail.html',{
            'question':q,'error_message':"You have not selected any option"
        })
    else:
        choice_pk.votes += 1
        choice_pk.save() 
        return HttpResponseRedirect(reverse('polls:result',args=(qid,)))