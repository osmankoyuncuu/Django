from django.db import models

# Create your models here.

class Profile(models.Model):
  username = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField()
  bio = models.TextField(blank=True, null=True)
  register_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.username
  
  class Meta:
    ordering = ["username"]
    verbose_name_plural = "User_Profile"