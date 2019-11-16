from django.shortcuts import render
from django.http import HttpResponse
from .models import policies

# Create your views here.
def index(request):

    Policies=policies.objects.all()[:10]
    context={
        'title':'Policies',
        'policies': Policies
    }
    #return HttpResponse('Hello from policies')
    return render(request,'policies/index.html', context)
def details(request, id):
    policy=policies.objects.get(id=id)
    context={
        'policy': policy
    }
    return render(request,'policies/details.html', context)