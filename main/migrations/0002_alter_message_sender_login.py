# Generated by Django 4.0.2 on 2022-02-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender_login',
            field=models.CharField(max_length=50, verbose_name='Логин отправителя*'),
        ),
    ]