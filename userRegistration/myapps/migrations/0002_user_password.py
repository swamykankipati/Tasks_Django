# Generated by Django 2.2.7 on 2020-05-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=15),
        ),
    ]
