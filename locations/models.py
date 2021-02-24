from django.db import models
from django.utils.text import slugify

class State(models.Model):
    name = models.CharField(verbose_name='الولاية', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(State, self).save(*args, **kwargs)

class Locality(models.Model):
    name = models.CharField(verbose_name='المحلية', max_length=50)
    state = models.ForeignKey(State, verbose_name='الولاية' , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Locality, self).save(*args, **kwargs)

class Unity(models.Model):
    name = models.CharField(verbose_name='الوحدة الادارية', max_length=50)
    locality = models.ForeignKey(Locality, verbose_name='المحلية', on_delete=models.CASCADE)
    state = models.ForeignKey(State, verbose_name='الولاية' , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Unity, self).save(*args, **kwargs)

class City(models.Model):
    name = models.CharField(verbose_name='المدينة', max_length=50)
    unity = models.ForeignKey(Unity, verbose_name='الوحدة الادارية', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name='المحلية', on_delete=models.CASCADE)
    state = models.ForeignKey(State, verbose_name='الولاية' , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(City, self).save(*args, **kwargs)
