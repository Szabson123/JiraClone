# Generated by Django 5.1.4 on 2024-12-09 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_userproject_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to='project.project'),
        ),
    ]
