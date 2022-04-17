# Generated by Django 4.0.2 on 2022-04-16 16:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=30, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 18, 16, 32, 26, 834845, tzinfo=utc), null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужчина'), ('W', 'Женщина')], max_length=2, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]