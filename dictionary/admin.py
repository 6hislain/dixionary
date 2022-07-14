from django.contrib import admin
from .models import (
    Word,
    Language,
    Definition,
    DefinitionLike,
    Translation,
    TranslationLike,
)

# Register your models here.
admin.site.register(Word)
admin.site.register(Language)
admin.site.register(Definition)
admin.site.register(Translation)
admin.site.register(DefinitionLike)
admin.site.register(TranslationLike)
