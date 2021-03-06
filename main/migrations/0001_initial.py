# Generated by Django 4.0.2 on 2022-02-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_login', models.CharField(max_length=50, verbose_name='Логин отправителя')),
                ('email', models.EmailField(max_length=100, verbose_name='Email отправителя*')),
                ('topic_letter', models.CharField(max_length=200, verbose_name='Тема письма*')),
                ('text_message', models.TextField(max_length=1500, verbose_name='Текст сообщения*')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
