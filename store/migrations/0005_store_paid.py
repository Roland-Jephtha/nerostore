# Generated by Django 4.2.3 on 2023-11-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_options_remove_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='paid',
            field=models.BooleanField(default=True, null=True),
        ),
    ]