from django.db import models
from django.utils import timezone

def three_days():
    return timezone.now() + timezone.timedelta(days=3)

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=three_days)

    # class Meta:
    #     ordering = ['due_date']

    def __str__(self):
        return self.title #f"{self.title}: due {self.due_date}"



        