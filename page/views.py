from django.shortcuts import render
from page.models import Application

# Create your views here.
def home(request):
    return render(request, 'home.html')

def apply(request):
    if request.method == 'POST':
        application = Application.objects.get(user=request.user)
        application.user = request.user
        application.field = request.POST['field']
        application.answers = {
            'answer1': request.POST['answer1'],
            'answer2': request.POST['answer2'],
            'answer3': request.POST['answer3'],
            'answer4': request.POST['answer4']
        }
        if 'portfolio' in request.FILES:
            application.portfolio = request.FILES['portfolio']
        application.date = request.POST['date']

        if request.POST['btn'] == 'save':
            application.is_submit = False
        else:
            application.is_submit = True
        application.save()
        return render(request, 'complete.html')
    else:
        try:
            myapplication = request.user.application
            if myapplication.is_submit == True:
                return render(request, 'home.html')
            answer1 = myapplication.answers['answer1']
            answer2 = myapplication.answers['answer2']
            answer3 = myapplication.answers['answer3']
            answer4 = myapplication.answers['answer4']

            return render(request, 'apply.html',
                          {'answer1': answer1, 'answer2': answer2, 'answer3': answer3, 'answer4': answer4})
        except Application.DoesNotExist:
            return render(request, 'apply.html')

def complete(request):
    return render(request, 'complete.html')

def intro(request):
    return render(request, 'intro.html')

def curriculum(request):
    return render(request, 'curriculum.html')