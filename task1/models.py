from django.db import models
from django.urls import reverse

class Buyer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя пользователя')
    balance = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Баланс')
    age = models.IntegerField(verbose_name='Bозраст пользователя')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return reverse('game_detail', args=[self.id])


class Game(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    title = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    size = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Размер файла')  # размер файлов игры
    description = models.TextField(blank=True, verbose_name='Описание')
    age_limited = models.BooleanField(blank=False,
                                          default=False)  # ограничение возраста 18 + (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, blank=True, related_name='game')

    def __str__(self):
        return self.title
