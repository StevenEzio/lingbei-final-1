# Generated by Django 2.1.2 on 2018-12-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20181205_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='url',
            field=models.TextField(default=' '),
        ),
    ]
