# Generated by Django 5.1.4 on 2024-12-12 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='to_do_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_do_item', to='base.todolist'),
        ),
    ]