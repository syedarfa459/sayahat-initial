# Generated by Django 3.1.2 on 2021-04-28 07:12

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
            name='AdventureClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('contact', models.CharField(default='', max_length=11)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('club_image', models.ImageField(null=True, upload_to='AdventureClub/Club_Images')),
                ('club_address', models.CharField(max_length=80)),
                ('city', models.CharField(default='', max_length=25)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdventureEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('overview', models.CharField(default='', max_length=120)),
                ('image', models.ImageField(null=True, upload_to='AdventureClub/AdventureEventPics')),
                ('featured', models.BooleanField(default=False)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('start_point', models.CharField(default='', max_length=70, null=True)),
                ('destination', models.CharField(default='', max_length=70, null=True)),
                ('event_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AdventureClub.adventureclub')),
            ],
        ),
        migrations.CreateModel(
            name='TouristReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tourist_review', models.CharField(max_length=256)),
                ('adventureevent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureClub.adventureevent')),
                ('tourist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(max_length=70, null=True)),
                ('destination', models.CharField(max_length=70, null=True)),
                ('booked_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdventureClub.adventureevent')),
            ],
        ),
    ]