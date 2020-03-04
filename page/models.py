from django.db import models
from account.models import User
from jsonfield import JSONField

# Create your models here.

class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=15, blank=True)
    answers = JSONField(default={})
    portfolio = models.FileField(blank=True)
    date = models.CharField(max_length=15, blank=True)
    is_submit = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
    