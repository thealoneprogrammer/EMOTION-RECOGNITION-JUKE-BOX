from django.db import models


# Create your models here.
class Auth(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name
