# Generated by Django 4.1.4 on 2022-12-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=12)),
                ('dateTime', models.DateTimeField()),
                ('otp', models.CharField(max_length=10)),
            ],
        ),
    ]