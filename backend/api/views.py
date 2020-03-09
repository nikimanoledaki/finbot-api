from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UserInput
from . import bot
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 

def index(request):
  user_input = list(UserInput.objects.all())[-1].text
  output = predict(user_input)
  return HttpResponse(output)

def predict(user_input):
  if isinstance(bot.chat(user_input), str):
    return bot.chat(user_input)
  else:
    return JsonResponse(bot.chat(user_input))

