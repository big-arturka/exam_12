# Generated by Django 2.2 on 2021-01-23 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210123_1004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'verbose_name': 'Друг', 'verbose_name_plural': 'Друзья'},
        ),
    ]
