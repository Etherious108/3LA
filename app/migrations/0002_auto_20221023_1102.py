# Generated by Django 3.0 on 2022-10-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default=1234, verbose_name='OTP'),
        ),
        migrations.AddField(
            model_name='user',
            name='pattern_order',
            field=models.CharField(default='123', max_length=3, verbose_name='Sequence'),
        ),
    ]
