from django.db import models
import datetime

# Create your models here.
# class todo(models.Model):
#     name = models.CharField('名称',max_length = 30)
#     age = models.CharField('年龄',max_length = 5)
#     number = models.IntegerField('工号')
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering = ['name']
#
#     class Admin:
#         pass


#
class List(models.Model):

  title = models.CharField(max_length=250, unique=True)

  def __str__(self):

    return self.title

  class Meta:

    ordering = ['title']

  class Admin:

    pass



PRIORITY_CHOICES = (

  (1, 'Low'),

  (2, 'Normal'),

  (3, 'High'),

)


class Item(models.Model):

  title = models.CharField(max_length=250)

  created_date = models.DateTimeField(default=datetime.datetime.now)

  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

  completed = models.BooleanField(default=False)

  todo_list = models.ForeignKey(List,on_delete=models.CASCADE )

  def __str__(self):

    return self.title

  class Meta:

    ordering = ['-priority', 'title']

  class Admin:

    pass