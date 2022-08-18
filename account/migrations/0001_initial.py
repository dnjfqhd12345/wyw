# Generated by Django 3.1.3 on 2022-07-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('favorites_1', models.CharField(choices=[('백엔드', '백엔드'), ('프론트엔드', '프론트엔드'), ('Andriod', 'Andriod'), ('iOS', 'iOS')], default='', max_length=200)),
                ('favorites_2', models.CharField(choices=[('백엔드', '백엔드'), ('프론트엔드', '프론트엔드'), ('Andriod', 'Andriod'), ('iOS', 'iOS')], default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
