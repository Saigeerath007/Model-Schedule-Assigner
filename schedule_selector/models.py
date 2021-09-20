import json
from django.db import models
from django.contrib.auth.models import User
from .forms import NewUserForm


# Create your models here.


class TimeTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    schedule = models.IntegerField(null=True, blank=True)
    pr_no = models.IntegerField(null=True, blank=True)
    academic_year = models.DateTimeField(auto_now_add=True)
    schedule_assigned = models.BooleanField(default=False)
    selected_pref = models.CharField(max_length=200, null=True, blank=True)
    pref_given = models.BooleanField(default=False)

    def get_pref(self, x):
        self.selected_pref = json.dumps(x)

    def __str__(self):
        if self.schedule_assigned:
            return self.schedule
        return str("TimeTable Unassigned")

    class Meta:
        db_table = 'Schedule'
