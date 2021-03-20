from django.db import models
from django.conf import settings
from django.contrib.auth import models as auth_models

#class Profile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #date_of_birth = models.DateField(blank=True, null=True)
    #photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    #def __str__(self):
        #return 'Profile for user {}'.format(self.user.username)


class UserExtend(models.Model):
    user = models.OneToOneField(
        auth_models.User,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name='Пользватель'
    )
    
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=80,
        blank=True,
        default=''
    )
    
    country = models.CharField(
        verbose_name='Страна',
        max_length=80,
        blank=True,
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=80,
        blank=True,
        default=''
    )

    post_index = models.CharField(
        verbose_name='Почтовый индекс',
        max_length=80,
        blank=True,
        default=''
    )

    address1 = models.CharField(
        verbose_name='Адрес 1',
        max_length=120,
        blank=True,
        default=''
    )

    address2 = models.CharField(
        verbose_name='Адрес 2',
        max_length=120,
        blank=True,
        default=''
    )

    def __str__(self):
        return f'{self.user}'
