# Generated by Django 4.0.5 on 2022-06-24 11:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('definition', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('like_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=200)),
                ('flag', models.ImageField(default='blank-flag-picture.png', upload_to='flags')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('word_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('translation', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('like_count', models.IntegerField(default=0)),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.definition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='words')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('definition_count', models.IntegerField(default=0)),
                ('translation_count', models.IntegerField(default=0)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TranslationLike',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.translation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_user_id', models.IntegerField()),
                ('bio', models.TextField(blank=True)),
                ('word_count', models.IntegerField(default=0)),
                ('definition_count', models.IntegerField(default=0)),
                ('translation_count', models.IntegerField(default=0)),
                ('image', models.ImageField(default='blank-profile-picture.png', upload_to='profiles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DefinitionLike',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.definition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='definition',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.word'),
        ),
    ]
