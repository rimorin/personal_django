from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    created_date = models.DateTimeField('user created date')
    def __str__(self):
        return self.user_id