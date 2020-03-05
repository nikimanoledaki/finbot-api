from tastypie.resources import ModelResource
from api.models import UserInput, BotOutput
from tastypie.authorization import Authorization

class UserInputResource(ModelResource):
  class Meta:
    limit = 0
    max_limit = 0
    queryset = UserInput.objects.all()
    resource_name = 'user_input'
    authorization = Authorization()

class BotOutputResource(ModelResource):
  class Meta:
    limit = 0
    max_limit = 0
    queryset = BotOutput.objects.all()
    resource_name = 'bot_output'
    authorization = Authorization()