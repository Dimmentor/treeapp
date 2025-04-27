from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']