from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(primary_key = True, max_length = 20)
    Name = models.CharField(max_length = 20)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.Name
    
class Book(models.Model):
    ISBN = models.CharField(primary_key = True, max_length = 20)
    Title = models.CharField(max_length = 20)
    AuthorID = models.ForeignKey(Author,related_name = 'books')
    Publisher = models.CharField(max_length = 20)
    PublishDate = models.DateField()
    Price = models.FloatField()
    def __unicode__(self):
        return self.Title