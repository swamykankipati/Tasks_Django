# Generated by Django 3.0.5 on 2020-04-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_emp_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField(max_length=10)),
                ('empName', models.CharField(max_length=50)),
                ('empDesign', models.CharField(max_length=50)),
                ('salary', models.FloatField(null=True)),
            ],
        ),
    ]
