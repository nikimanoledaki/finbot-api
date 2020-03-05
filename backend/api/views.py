from django.shortcuts import render
from django.http import HttpResponse
from .models import BotOutput

def index(request):
  output = chat()
  return HttpResponse(output)

def chat():
  output = BotOutput.objects.create(text='I am a robot')
  return output
