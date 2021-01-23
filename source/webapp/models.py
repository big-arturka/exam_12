from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Message(models.Model):
    author: AbstractUser = models.OneToOneField(get_user_model(), related_name='author_message',
                                                on_delete=models.CASCADE, verbose_name='Отправитель')
    recipient: AbstractUser = models.OneToOneField(get_user_model(), related_name='recipient_message',
                                                   on_delete=models.CASCADE, verbose_name='Получатель')
    text = models.TextField(max_length=2000, verbose_name='Текст сообщения')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
