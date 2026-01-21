from django.db import models

class House(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    built_at = models.DateField()
    rooms = models.IntegerField()
    area = models.DecimalField(max_digits=6, decimal_places=2)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='house_images/', null=True, blank=True)

    def __str__(self):
        return self.title
