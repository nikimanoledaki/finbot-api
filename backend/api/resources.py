from tastypie.resources import ModelResource
from .models import UserInput
from tastypie.authorization import Authorization

class UserInputResource(ModelResource):
  class Meta:
    limit = 0
    max_limit = 0
    queryset = UserInput.objects.all()
    resource_name = 'user_input'
    authorization = Authorization()
