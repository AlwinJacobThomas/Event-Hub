# Generated by Django 4.0.6 on 2022-08-01 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=50, verbose_name='Event Name')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('e_date', models.DateField(auto_now_add=True, verbose_name='Event Date')),
                ('desc', models.TextField(verbose_name='Description')),
                ('p_limit', models.IntegerField(verbose_name='Participant Limit')),
                ('brochure', models.ImageField(null=True, upload_to=event.models.PathAndRename('event/'), verbose_name='Event Poster')),
                ('e_type', models.CharField(default='College Fest', max_length=188, verbose_name='Event Type')),
                ('reg_fee', models.CharField(default='Free', max_length=100, verbose_name='Registration Fee')),
                ('Venue', models.CharField(max_length=255)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('time', models.TimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]
