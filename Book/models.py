from django.db import models

# Create your models here.
# app name Book model Name Book
class BookActiveManager(models.Manager):
    def get_queryset(self): #quryset means all data
        return super(BookActiveManager,self).get_queryset().filter(is_deleted='N')
class BookInactiveManager(models.Manager):
    def get_queryset(self): #quryset means all data
        return super(BookInactiveManager,self).get_queryset().filter(is_deleted='Y')
class Book(models.Model):
    # id created by default Django
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    qty  =  models.IntegerField()
    price = models.FloatField() 
    is_published = models.BooleanField(default=False)
    is_deleted = models.CharField(max_length=1, default='N')
    low_priced = models.CharField(max_length=1, default='N')
    active_objects = BookActiveManager()
    inactive_objects = BookInactiveManager()
    objects = models.Manager() 

    def __str__(self):
        return f"{self.name}---{self.author}"
    class  Meta:
        db_table = "bookinfo"

