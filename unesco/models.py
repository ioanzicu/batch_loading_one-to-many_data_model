from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=512)
    justification = models.CharField(max_length=512)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Site name={self.name}, year={self.year}, description={self.description}, justification={self.justification}, category={self.category}, state={self.state}, region={self.region}, iso={self.iso}.'
