# Generated by Django 3.2.7 on 2021-10-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211003_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='top10',
            name='remains',
        ),
        migrations.AlterField(
            model_name='top10',
            name='tops',
            field=models.TextField(default=''),
        ),
    ]
