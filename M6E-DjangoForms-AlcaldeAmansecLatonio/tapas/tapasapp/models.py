# Johann Miguel S. Alcalde, 240150 ; Samantha Louise F. Amansec, 230286 ; Zale Sebastian S. Latonio, 242494
'''
We hereby attest to the truth of the following facts:

We have not discussed the Python code in our program with anyone
other than my instructor or the teaching assistants assigned to this course.

We have not used Python code obtained from another student, or
any other unauthorized source, whether modified or unmodified.

If any Python code or documentation used in our program was
obtained from another source, it has been clearly noted with citations in the
comments of our program.'''

from django.db import models

# Create your models here.

'''
class Dish(models.Model):
    name = models.CharField(max_length=300)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.name
'''

'''
2. Create an Account model with fields for a username and a password. Define get
methods as well (i.e. getUsername() and getPassword()) to retrieve the
values for these fields
'''
class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def getUsername():
        return username

    def getPassword():
        return password