# Generated by Django 2.1.2 on 2018-12-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practise', '0003_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='Query',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
