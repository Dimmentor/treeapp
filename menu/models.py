from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']