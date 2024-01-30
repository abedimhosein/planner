# Generated by Django 4.2.9 on 2024-01-30 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='skills', to='skills.board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='queues', to='skills.board')),
            ],
            options={
                'unique_together': {('title', 'board')},
            },
        ),
    ]
