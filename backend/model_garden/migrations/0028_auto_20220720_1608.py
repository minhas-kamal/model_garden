# Generated by Django 3.0.6 on 2022-07-20 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_garden', '0027_mediaasset_local_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='bucket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='model_garden.Bucket'),
        ),
    ]
