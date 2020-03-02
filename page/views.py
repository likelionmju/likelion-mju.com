from django.shortcuts import render
from page.models import Application

# Create your views here.
def home(request):
    return render(request, 'home.html')

def apply(request):
    if request.method == 'POST':
        # delete the old application
        Application.objects.filter(user=request.user).delete()

        answers = {'answer1': request.POST['answer1'], 'answer2': request.POST['answer2'], 'answer3': request.POST['answer3'], 'answer4': request.POST['answer4']}
        application = Application()
        application.user = request.user
        application.answers = answers
        if request.POST['btn'] == 'save':
            application.is_submit = False
        else:
            application.is_submit = True
        application.save()
        return render(request, 'complete.html')
    else:
        try:
            myapplication = request.user.application
            answer1 = myapplication.answers['answer1']
            answer2 = myapplication.answers['answer2']
            answer3 = myapplication.answers['answer3']
            answer4 = myapplication.answers['answer4']
            return render(request, 'apply.html',
                          {'answer1': answer1, 'answer2': answer2, 'answer3': answer3, 'answer4': answer4})
        except Application.DoesNotExist:
            return render(request, 'apply.html')