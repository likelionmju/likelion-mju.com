from django.db import models
from account.models import User
from jsonfield import JSONField

# Create your models here.

class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answers = JSONField(default={})
    portfolio = models.FileField(blank=True)
    is_submit = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
    