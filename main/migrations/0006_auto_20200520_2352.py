# Generated by Django 3.0.6 on 2020-05-20 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200520_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='matches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Match'),
        ),
    ]