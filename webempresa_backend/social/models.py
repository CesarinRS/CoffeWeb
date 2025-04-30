from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Clave", max_length=50, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=100)
    url = models.URLField(verbose_name="Enlace", max_length=500, blank=True, null=True)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ("name",)

    def __str__(self):
        return self.name

