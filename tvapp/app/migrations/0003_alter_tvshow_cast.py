# Generated by Django 4.1.5 on 2023-02-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tvshow_cast_alter_tvshow_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='cast',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]