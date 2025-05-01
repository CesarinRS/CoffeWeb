from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ("title",)

    def __str__(self):
        return self.title