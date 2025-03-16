from PIL import Image
from django.db import models
from slugify import slugify
import uuid

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='characters/')  # Указываем папку для загрузки изображений
    votes_for = models.PositiveIntegerField(default=0)
    votes_against = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Если объект уже существует в базе данных
        if self.pk:
            old_character = Character.objects.get(pk=self.pk)
            # Если изображение изменилось
            if old_character.image != self.image:
                old_character.image.delete(save=False)  # Удалить старое изображение
                # Генерируем новое имя файла
                unique_id = uuid.uuid4().hex[:6]  # Уникальный идентификатор
                self.image.name = f'characters/{slugify(self.name)}_{unique_id}.jpg'
        else:
            # Если объект создается впервые, генерируем новое имя файла
            unique_id = uuid.uuid4().hex[:6]  # Уникальный идентификатор
            self.image.name = f'characters/{slugify(self.name)}_{unique_id}.jpg'

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Удалить изображение при удалении персонажа
        self.image.delete(save=False)
        super().delete(*args, **kwargs)