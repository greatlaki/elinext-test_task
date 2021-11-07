from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='Book title')
    author = models.CharField(max_length=100, verbose_name='Author')
    written_year = models.IntegerField(verbose_name='Book written year')
    birth_year = models.IntegerField(verbose_name='Author birth year')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title', 'author']
        unique_together = (
            ('title', 'author'),
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    first_name = models.TextField(max_length=30, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Last name')
    phone_number = models.DateField(null=True, blank=True, verbose_name='Phone number')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Photo')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

