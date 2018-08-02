# Generated by Django 2.0.6 on 2018-07-01 01:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='brand',
            index=models.Index(fields=['name'], name='stashology__name_5ddb05_idx'),
        ),
        migrations.AddIndex(
            model_name='brand',
            index=models.Index(fields=['created_at'], name='stashology__created_80c3d3_idx'),
        ),
    ]