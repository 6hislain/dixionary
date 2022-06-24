from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_user_id = models.IntegerField()
    bio = models.TextField(blank=True)
    word_count = models.IntegerField(default=0)
    definition_count = models.IntegerField(default=0)
    translation_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="profiles", blank=True)

    def __str__(self):
        return self.user.username


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    language = models.CharField(max_length=200)
    flag = models.ImageField(upload_to="flags", blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    word_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.language


class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    word = models.CharField(max_length=200)
    image = models.ImageField(upload_to="words", blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    definition_count = models.IntegerField(default=0)
    translation_count = models.IntegerField(default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.word


class Definition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    definition = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    like_count = models.IntegerField(default=0)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition


class DefinitionLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(default=datetime.now)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition.definition


class Translation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    translation = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    like_count = models.IntegerField(default=0)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.translation


class TranslationLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(default=datetime.now)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.translation.translation
