# Generated by Django 3.1.3 on 2022-07-29 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20220729_2248'),
        ('wyw', '0022_auto_20220728_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='author_avatar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_question', to='account.profile'),
            preserve_default=False,
        ),
    ]
