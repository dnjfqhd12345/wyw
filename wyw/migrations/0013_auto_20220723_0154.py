# Generated by Django 3.1.3 on 2022-07-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyw', '0012_auto_20220723_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]