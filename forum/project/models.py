from django.db import models
# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=100, null=True)
    short_description = models.TextField(max_length=200, null=True)
    description = models.TextField(max_length=250, null=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    status = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)


class ProjectQueue(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    interested_devs = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    dev_price = models.IntegerField(null=True)
    acceptance = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


