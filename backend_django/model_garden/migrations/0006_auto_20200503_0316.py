# Generated by Django 3.0.5 on 2020-05-03 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_garden', '0005_auto_20200501_2236'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BucketItem',
            new_name='Dataset',
        ),
        migrations.RenameField(
            model_name='mediaasset',
            old_name='bucket_item',
            new_name='dataset',
        ),
    ]
