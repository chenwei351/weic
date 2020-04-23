from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField('名称',max_length = 30)
    age = models.CharField('年龄',max_length = 5)
    number = models.IntegerField('工号')
    
    def __str__(self):
        return self.name