# Generated by Django 2.2 on 2021-01-23 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_message', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_message', to=settings.AUTH_USER_MODEL, verbose_name='Получатель'),
        ),
    ]
