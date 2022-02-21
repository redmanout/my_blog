from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    CHOICES = (
        ('male', 'Мужской пол'),
        ('female', 'Женский пол')
    )

    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    gender = models.CharField(
        verbose_name='Пол пользователя',
        max_length=30,
        choices=CHOICES,
        default='male'
    )
    mailing_agreement = models.BooleanField(
        default=False,
        verbose_name='Соглашение на отправку уведомлений на почту'
    )
    img = models.ImageField(
        'Фото пользователя',
        default='default.png',
        upload_to='user_images'
    )

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
