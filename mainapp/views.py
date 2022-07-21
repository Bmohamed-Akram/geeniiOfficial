from pkgutil import ImpImporter
from django.shortcuts import render
from mainapp.models import project,questions
from django.http import JsonResponse,HttpResponse
# Create your views here.

def page(request):
    projects = project.objects.all()
    return render(request,'index.html',{'projects':projects})

def getinfo(request):
    projects = project.objects.all()
    return JsonResponse({"projects":list(projects.values())})

def ask(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        the_question = request.POST['question']

        question = questions.objects.create(userName=name,email=email,mobileNum=number,question=the_question)
        question.save()

        return HttpResponse("you will get your reply as email soon Thank you")

