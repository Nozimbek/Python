# Generated by Django 3.0.6 on 2020-08-08 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200807_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='available_seats',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='start_time',
        ),
        migrations.CreateModel(
            name='MoviePlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('available_seats', models.IntegerField()),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='catalog.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('secret_number', models.CharField(max_length=255)),
                ('for_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='catalog.MoviePlay')),
            ],
        ),
    ]
