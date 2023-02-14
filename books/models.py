from django.db import models



class Book(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2400, default="")
    book_file = models.FileField(upload_to="books/")