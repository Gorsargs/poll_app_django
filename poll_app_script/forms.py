from django import forms
from django.forms import ModelForm,TextInput
from .models import Question



class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name','choice1','choice2',
                'choice3','choice4','choice5',
                'choice6','choice7','choice8',
                'choice9','choice10','choice11',
                'choice12','choice13','choice14',
               ]
        widgets = {}
        for i in fields:
            if not('choice' in i):
                widgets[i] = forms.Textarea(attrs={ 
                    'type' : 'text', 
                    'class' : 'question-field', 
                    'value' : '',
                    'id' : 'question-field',
                    'placeholder': 'Your Question',})
                
            else:
                widgets[i] = TextInput(attrs={ 
                    'type' : 'text', 
                    'class' : 'form-control  form-control-sm',
                    'value' : '',
                    'id':f"choice{''.join(filter(str.isdigit, i))}",
                    'placeholder' : f"Option {''.join(filter(str.isdigit, i))}",
                    'onchange':'submitOnOff()'
                    })


                
