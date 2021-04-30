from django.db import models


class Region(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('-name', )

    def __str__(self):
        return self.name


class City(models.Model):

    region = models.ForeignKey(Region,
                               related_name='region',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

