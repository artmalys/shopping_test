# Generated by Django 2.2.2 on 2019-06-19 17:55

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='phone',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, verbose_name='phone number'),
        ),
    ]
