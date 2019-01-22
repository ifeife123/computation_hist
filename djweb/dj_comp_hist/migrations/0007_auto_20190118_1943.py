# Generated by Django 2.1.5 on 2019-01-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_comp_hist', '0006_auto_20190117_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='author', to='dj_comp_hist.Person'),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='recipient',
            field=models.ManyToManyField(blank=True, related_name='recipient', to='dj_comp_hist.Person'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=191),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(blank=True, max_length=191),
        ),
        migrations.AlterField(
            model_name='organization',
            name='location',
            field=models.CharField(blank=True, max_length=191),
        ),
        migrations.AlterField(
            model_name='person',
            name='first',
            field=models.CharField(blank=True, max_length=191),
        ),
        migrations.AlterField(
            model_name='person',
            name='last',
            field=models.CharField(blank=True, max_length=191),
        ),
        migrations.AlterField(
            model_name='person',
            name='organization',
            field=models.ManyToManyField(blank=True, to='dj_comp_hist.Organization'),
        ),
    ]