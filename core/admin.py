from django.contrib import admin
from .models import Profile, Post, PostLike, FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(FollowersCount)
