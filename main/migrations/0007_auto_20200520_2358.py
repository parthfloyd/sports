# Generated by Django 3.0.6 on 2020-05-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200520_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='matches',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='matches',
            field=models.ManyToManyField(to='main.Match'),
        ),
    ]