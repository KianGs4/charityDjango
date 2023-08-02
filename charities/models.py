from django.db import models
from accounts.models import User
from django.db.models import *


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(default=0,
                                          choices=((0, 'Beginner'), (1, 'Intermediate'), (2, 'Professional')))
    free_time_per_week = models.PositiveIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)




class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return Task.objects.filter(charity__user__exact=user)

    def related_tasks_to_benefactor(self, user):
        return Task.objects.filter(assigned_benefactor__user__exact=user)

    def all_related_tasks_to_user(self, user):
        return Task.objects.filter(Q(charity__user__exact=user) | Q(assigned_benefactor__user__exact=user) |
                                   Q(state__exact='P'))



class Task(models.Model):
    STATE_CHOICES = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(choices=(('M', 'Male'), ('F', 'Female')), max_length=1)
    state = models.CharField(choices=STATE_CHOICES, max_length=1)
    title = models.CharField(max_length=60)
    objects = TaskManager()

