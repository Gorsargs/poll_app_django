from django.shortcuts import render,redirect
from .classes import Choises
from .forms import QuestionForm
from .models import Question
import json


def index(request):
    questions = Question.objects.all()
    list_of_questions = []
    for question in questions:
        list_of_questions.append(question)

    context = {'questions' : list_of_questions}
    return render(request,'questions/index.html',context)


def question(request,pk):
    context = {}
    return render(request,'questions/question.html',context)

def create(request):
    for_json = {}
    form = QuestionForm()
    if request.method == 'POST':
        if 'create' in request.POST:
            form_dict = request.POST.dict()
            length = len([i for i in form_dict.keys() if 'choice' in i])
            
            for i in range(1,length+1):
                if len(form_dict[f'choice{i}']) == 0:
                    form_dict[f'choice{i}'] = f"Empty Choice {i}"

            form = QuestionForm(form_dict)
            if form.is_valid():
                form.save()
                return redirect('/')

    form = QuestionForm()
    form_list = []
    

    for i in range(1,len(form.__dict__)+1):
        form_list.append(form[f"choice{i}"])
            
    context = {'form':form,'form_list':form_list,}
    return render(request, 'questions/create.html',context)

def view_poll(request,pk):
    poll = Question.objects.get(id = pk)
    poll_dict = poll.__dict__
    length = len([i for i in poll_dict.keys() if 'choice' in i])
    polls = [poll_dict[f"choice{i}"] for i in range(1,length//2+1)]
    if request.method == 'POST':
        # try:
        selected_option = request.POST['option']
        print(selected_option)
        for i in poll_dict.keys():
            if "choice" in i:
                if poll_dict[i] == selected_option:
                    print(i)
                    digit = ''.join(filter(str.isdigit,i))
                    poll_dict[f"choice_answer_{digit}"] += 1
                    poll.save()
                    return redirect(f'/result/{pk}')
        # except:c
            # return redirect(f'/vote/{pk}')
        
            
    
    context = {'poll':poll,'polls':polls}
    return render(request,'questions/vote.html',context)

def result(request,pk):
    poll = Question.objects.get(id = pk)
    poll_dict = poll.__dict__
    length = poll_dict['choice_count']
    polls = {}
    poll_sum = sum([poll_dict[f"choice_answer_{i}"] for i in range(1,15)])
    for  i in range(1,15):
        if poll_sum > 0:
            polls[poll.__dict__[f"choice{i}"]] = round((poll_dict[f'choice_answer_{i}']/poll_sum)*100,2)
        else:
            polls[poll.__dict__[f"choice{i}"]] = poll_dict[f'choice_answer_{i}']
    context = {'poll':poll,'polls':polls,}
    return render(request,'questions/result.html',context)


def delete_poll(request, pk):
    print(request)
    try:
        Question.objects.get(id = pk).delete()
    except:
        return redirect('/')
    return redirect('/')