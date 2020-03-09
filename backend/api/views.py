from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInput
from . import bot

def index(request):
  user_input = list(UserInput.objects.all())[-1].text
  output = predict(user_input)
  return HttpResponse(output)

def predict(user_input):
  return bot.chat(user_input)
