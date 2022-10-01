from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from django.contrib import messages

# CRUD DEVELOPERS

#------ Create ------

def createDev(request):
    name = request.POST['nameInput']
    age = request.POST['ageInput']
    skill = request.POST['skillInput']

    developer = Developer.objects.create(
        name=name, age=age, skill=skill)
    messages.success(request, 'User: ' + name +' ¡Save Success !')
    return redirect('/')


#------ List ------
def listDev(request):
    developers = Developer.objects.all()
    return render(request, "index.html", {"developers": developers})


#------ Edit ------
def editDev(request, slug):
    developer = Developer.objects.get(slug=slug)

    name = request.POST.get('nameInput')
    age = request.POST.get('ageInput')
    skill = request.POST.get('skillInput')
    if request.method == 'POST':

        developer.name = name
        developer.age = age
        developer.skill = skill
        developer.save()
        messages.success(request, 'User: ' + name +' ¡Edit Success!')
        return redirect('/')

    return render (request, "edit.html", {"developer": developer})

#------ Delete ------
def deleteDev(request, slug):
    developer = Developer.objects.get(slug=slug)

    developer.delete()
    messages.success(request, '¡Developer Deleted!')
    return redirect('/')  
