# Generated by Django 4.0.2 on 2022-02-18 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_contentfile_customer_alter_contentfile_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentfile',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gems', to='deals.gems'),
        ),
    ]