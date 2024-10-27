from PIL import Image
from django.db import models
from django.utils.text import slugify


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    votes_for = models.PositiveIntegerField(default=0)
    votes_against = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:  # Если объект уже существует в базе данных
            old_character = Character.objects.get(pk=self.pk)
            if old_character.image != self.image:  # Если изображение изменилось
                old_character.image.delete(save=False)  # Удалить старое изображение

        # Изменить имя файла изображения на основе имени персонажа
        self.image.name = f'characters/{slugify(self.name)}.jpg'


        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Удалить изображение при удалении персонажа
        self.image.delete(save=False)
        super().delete(*args, **kwargs)
