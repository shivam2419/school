# Generated by Django 4.2.6 on 2024-06-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0013_activity_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_desc',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
