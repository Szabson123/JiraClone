# Generated by Django 5.1.4 on 2024-12-19 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_userproject_project'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='project.status')),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to='project.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(through='project.UserTask', to=settings.AUTH_USER_MODEL),
        ),
    ]
