from django.db import models

# Create your models here.
class video(models.Model):
    name=models.TextField()
    file=models.FileField(upload_to="Documents\Kuliah Smt 5\Pemlan")
    image=models.ImageField(upload_to="Documents\Kuliah Smt 5\Pemlan\imek")

    def __str__(self):
        return self.name