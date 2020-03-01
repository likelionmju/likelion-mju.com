from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def apply(request):
    return render(request, 'apply.html')
