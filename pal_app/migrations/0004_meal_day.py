# Generated by Django 2.2.3 on 2019-07-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pal_app', '0003_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='day',
            field=models.DateField(auto_now=True),
        ),
    ]
