# Generated by Django 2.1.5 on 2019-01-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_comp_hist', '0015_auto_20190124_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='first_page',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='last_page',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='page',
            name='image_path',
            field=models.CharField(blank=True, max_length=191),
        ),
    ]
