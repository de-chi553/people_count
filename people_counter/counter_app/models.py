from django.db import models

class PeopleCount(models.Model):
    count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"People Count: {self.count} (Updated at: {self.updated_at})"
