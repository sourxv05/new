# Generated by Django 4.2.5 on 2023-09-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-02-22'),
            preserve_default=False,
        ),
    ]
