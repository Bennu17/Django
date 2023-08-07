from django.db import models

class sample(models.Model):
         name=models.CharField(max_length=100,null=False,blank=False)
         age=models.IntegerField(null=False,blank=False)
         gender=models.CharField(max_length=30,null=False,blank=False)
         
         def __str__(self):
                  return self.name

