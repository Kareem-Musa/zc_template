from django.db import models
from locations.models import State, Locality, Unity
from django.utils.text import slugify

class Hquarter(models.Model):
    name = models.CharField(verbose_name='الامانة', max_length=50)
    state = models.ForeignKey(State, verbose_name='الولاية', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Hquarter, self).save(*args, **kwargs)

class Sector(models.Model):
    name = models.CharField(verbose_name='القطاع', max_length=50)
    state = models.ForeignKey(State, verbose_name='الولاية', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name='المحلية', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Sector, self).save(*args, **kwargs)

class Office(models.Model):
    name = models.CharField(verbose_name='المكتب', max_length=50)
    state = models.ForeignKey(State, verbose_name='الولاية', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name='المحلية', on_delete=models.CASCADE)
    unity = models.ForeignKey(Unity, verbose_name='الوحدة الادارية', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Office, self).save(*args, **kwargs)
