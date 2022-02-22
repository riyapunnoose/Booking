# Generated by Django 3.2.9 on 2022-02-11 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='admin', max_length=20)),
                ('password', models.CharField(default='1234', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeid', models.CharField(default='', max_length=100)),
                ('eventid', models.CharField(max_length=60)),
                ('aboutid', models.TextField()),
                ('date', models.DateTimeField()),
                ('EntryFeeid', models.IntegerField()),
                ('categoryid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ids', models.IntegerField()),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nos', models.IntegerField()),
                ('Evnt_id', models.CharField(max_length=300)),
                ('total', models.IntegerField(default='')),
                ('date_now', models.DateTimeField(auto_now=True)),
                ('uuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]