# Generated by Django 5.1.6 on 2025-03-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_rename_created_task_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_at',
            new_name='created',
        ),
    ]
