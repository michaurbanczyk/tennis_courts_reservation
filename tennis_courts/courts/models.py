from django.db import models


class City(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Club(models.Model):

    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    zip_code = models.CharField(max_length=400)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    main_image = models.ImageField(upload_to='clubs', blank=True)
    slug = models.SlugField(max_length=400, db_index=True)





