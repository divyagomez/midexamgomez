from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Position, Vote
from .forms import CandidateModelForm, PositionModelForm
from django.utils import timezone

# Create your views here.

def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)



def help(request):
    return HttpResponse('This is the help page')



def candidate_detail(request, candidate_id):
    context = {}
    context['candidates'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'candidate_detail.html')



def candidate_update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        # question = Question.objects.get(id=question_id)
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate updated')
        else:
            context['form'] = form
            return render(request, 'candidate_update.html', context)
    else:
        context['form'] = CandidateModelForm(instance=post)
        return render(request, 'candidate_update.html', context)





def candidate_create(request):
    context = {}
    #question = Question.objects.get(id=question_id)
    form = CandidateModelForm(initial={"date_created":timezone.now()})

    if request.method == 'POST':

        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('votes:index')


    return render(request, 'candidate_create.html', {"form":form})




def position_create(request):
    context = {}
    #question = Question.objects.get(id=question_id)
    form = PositionModelForm(initial={"date_created":timezone.now()})

    if request.method == 'POST':

        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('votes:index')


    return render(request, 'position_create.html', {"form":form})





# def vote(request, vote_id):
#     context = {}
#     vote = Vote.objects.get(id=vote_id)
#
#     if request.method == 'POST':
#         # question = Question.objects.get(id=question_id)
#         form = VoteModelForm(request.POST, instance=post)
#         if form.is_valid():
#             vote = form.save()
#             vote.post = post
#             vote.save()
#             return HttpResponse('Voted')
#         else:
#             context['form'] = form
#             return render(request, 'vote.html', context)
#     else:
#         context['form'] = VoteModelForm(instance=post)
#         return render(request, 'vote.html', context)
