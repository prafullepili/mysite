# Generated by Django 3.2.7 on 2021-10-23 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WxPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coins',
            old_name='withCurrency',
            new_name='fullname',
        ),
    ]
