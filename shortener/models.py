from django.db import models

class ShortLinkModel(models.Model):
    origin_url = models.TextField()
    short_url = models.TextField()
    hash_value = models.IntegerField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.origin_url