# Generated by Django 4.0.4 on 2022-06-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_products_alter_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pick_available',
            field=models.BooleanField(default=True),
        ),
    ]
