from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    progress = models.IntegerField(default=0)
    status = models.CharField(default='success', max_length=20)

    def __unicode__(self):
        return self.name

class Flujo(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'flujos'

class Actividad(models.Model):
    name = models.CharField(max_length=20)
    flujo = models.ForeignKey(Flujo)

    def __unicode__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'flujo'
        verbose_name_plural = 'actividades'
