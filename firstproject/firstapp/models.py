from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    dicr=models.TextField()
    def __str__(self):
        return self.name
class person(models.Model):
    name1=models.CharField(max_length=15)
    img1=models.ImageField(upload_to='p1')
    dicr1=models.TextField()

    def __str__(self):
        return self.name1
