from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Message(models.Model):
    author: AbstractUser = models.ForeignKey(get_user_model(), related_name='author_message',
                                                on_delete=models.CASCADE, verbose_name='Отправитель')
    recipient: AbstractUser = models.ForeignKey(get_user_model(), related_name='recipient_message',
                                                   on_delete=models.CASCADE, verbose_name='Получатель')
    text = models.TextField(max_length=2000, verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.author}-{self.recipient}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
