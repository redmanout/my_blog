from django.db import models


class Message(models.Model):
    sender_login = models.CharField(
        max_length=50,
        verbose_name='Логин отправителя'
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Email отправителя*'
    )
    topic_letter = models.CharField(
        max_length=200,
        verbose_name='Тема письма*'
    )
    text_message = models.TextField(
        max_length=1500,
        verbose_name='Текст сообщения*'
    )

    def __str__(self):
        return f'Пользователь с логином {self.sender_login} отправил письмо на email:{self.email}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
