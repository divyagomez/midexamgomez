# Generated by Django 2.1 on 2019-01-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_auto_20190130_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_datetime',
            field=models.DateTimeField(),
        ),
    ]
