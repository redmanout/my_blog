# Generated by Django 4.0.2 on 2022-02-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Мужской пол'), (2, 'Женский пол')], default=1, max_length=20, verbose_name='Пол пользователя'),
            preserve_default=False,
        ),
    ]
