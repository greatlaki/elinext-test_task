from django.db import models


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

