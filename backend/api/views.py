from django.shortcuts import render
from django.http import HttpResponse
from .models import BotOutput
from .models import UserInput


def index(request):
  user_input = UserInput.objects.all()[0].text
  output = chat()
  return HttpResponse(output + user_input)

def chat():
  return 'hello '
