from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='المستخدم', on_delete=models.CASCADE,
            blank=True, null=True)
    first = models.CharField(verbose_name='الاسم الاول', max_length=50, blank=True, null=True)
    last = models.CharField(verbose_name='الاسم الاخير', max_length=50, blank=True, null=True)
    photo = models.ImageField(verbose_name='الصورة', upload_to='photos/%Y/%m', blank=True, null=True)

    def __str__(self):
        return self.user
