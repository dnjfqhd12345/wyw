# Generated by Django 3.1.3 on 2022-07-30 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20220729_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='button.png', upload_to='media/'),
        ),
    ]
