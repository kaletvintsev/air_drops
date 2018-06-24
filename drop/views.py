from django.http import HttpResponse
from django.template import loader
from .models import Drop
from django.shortcuts import render


def drops(request):
    latest_question_list = Drop.objects.order_by('-pub_date')[:5]
    template = loader.get_template('drop/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    return render(request, "index.html")