# Generated by Django 4.0.2 on 2022-02-18 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0008_alter_contentfile_customer_alter_contentfile_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileModel',
        ),
    ]
