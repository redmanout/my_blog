# Generated by Django 4.0.2 on 2022-02-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mailing_agreement',
            field=models.BooleanField(default=False, verbose_name='Соглашение на отправку уведомлений на почту'),
        ),
    ]
