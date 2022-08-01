from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_user_id = models.IntegerField()
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="profiles/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.user.username()

    def word_count(self):
        return self.word_set.count()

    def definition_count(self):
        return self.definition_set.count()

    def translation_count(self):
        return self.translation_set.count()
