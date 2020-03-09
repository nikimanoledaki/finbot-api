from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInput
from . import bot
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 

def index(request):
  user_input = list(UserInput.objects.all())[-1].text
  output = predict(user_input)
  return HttpResponse(output)

def predict(user_input):
  print(bot.chat(user_input))
  return bot.chat(user_input)

