from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()                # data ra az databse megira
    template = loader.get_template('all_members.html')   
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))














# def members(request):
#     template = loader.get_template('btn.html')
#     return HttpResponse(template.render())

# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

# def chat(request):
#     template = loader.get_template('chat.html')
#     return HttpResponse(template.render())

# def images(request):
#     template = loader.get_template('images.html')
#     return HttpResponse(template.render())

# def videos(request):
#     template = loader.get_template('videos.html')
#     return HttpResponse(template.render())


# def map(request):
#     template = loader.get_template('map.html')
#     return HttpResponse(template.render())

# def news(request):
#     template = loader.get_template('news.html')
#     return HttpResponse(template.render())