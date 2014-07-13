from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from switches.models import Switch

class Index(View):
    def get(self, request):
        switches = Switch.objects.all()
        result = '<br> - '.join([switch.__str__() for switch in switches])
        return HttpResponse(result)  

def detail(request, switch_id):
    return HttpResponse("You're looking at Sprinkler %s." % switch_id)
