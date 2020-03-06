from django.db import models

class UserInput(models.Model):
  text = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s' % (self.text)

