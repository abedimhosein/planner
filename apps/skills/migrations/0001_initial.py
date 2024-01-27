# Generated by Django 4.2.9 on 2024-01-27 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.models.fields


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
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boards', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, utils.models.fields.AtWhenFields),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='skills', to='skills.board')),
            ],
            bases=(models.Model, utils.models.fields.AtWhenFields),
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='queues', to='skills.board')),
            ],
            options={
                'unique_together': {('title', 'board')},
            },
            bases=(models.Model, utils.models.fields.AtWhenFields),
        ),
    ]
