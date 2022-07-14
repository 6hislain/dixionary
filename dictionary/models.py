from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=200)
    flag = models.ImageField(upload_to="flags", blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    word_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.language

    def word_count(self):
        return self.word_set.count()


class Word(models.Model):
    word = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to="words", blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

    def definition_count(self):
        return self.definition_set.count()


class Definition(models.Model):
    definition = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition

    def like_count(self):
        return self.definitionlike_set.count()

    def translation_count(self):
        return self.translation_set.count()


class DefinitionLike(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition.definition


class Translation(models.Model):
    word = models.CharField(max_length=200)
    translation = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.translation

    def like_count(self):
        return self.translationlike_set.count()


class TranslationLike(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.translation.translation
