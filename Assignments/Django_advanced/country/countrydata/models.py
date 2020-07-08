from django.db import models

MNL = 50
MCL = 5


class Continent(models.Model):
    """
    Fields
    """
    name = models.CharField("name", max_length=MNL, unique=True)
    code = models.CharField("code", max_length=MCL, default="", unique=True)
    class Meta:
        ordering = ['name']

    """
    Methods
    """
    def __str__(self):
        return "%s, %s" % (self.name, self.code)

class Country(models.Model):
    name = models.CharField("name", max_length=MNL, unique=True)
    capital = models.CharField("capital", max_length=MNL)
    code = models.CharField("code", max_length=MCL, default="", unique=True)
    population = models.PositiveIntegerField("population")
    area = models.PositiveIntegerField("area")
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE,
        related_name="countries")
    class Meta:
        ordering = ['name']


    """
    Methods
    """
    def __str__(self):
        return "%s, %s" % (self.name, self.code)
