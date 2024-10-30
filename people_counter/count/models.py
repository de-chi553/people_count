from django.db import models

class PeopleCounter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Current People Count: {self.count}"
