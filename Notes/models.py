from django.db import models

# Create your models here.
class NotesController(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    success = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
