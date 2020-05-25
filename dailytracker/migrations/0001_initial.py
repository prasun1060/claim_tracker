# Generated by Django 3.0.6 on 2020-05-24 11:26

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
            name='DailyTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('claim_no', models.IntegerField()),
                ('billed_charges', models.FloatField()),
                ('benefit', models.FloatField()),
                ('market', models.CharField(choices=[('IN', 'Indiana'), ('MD', 'Maryland'), ('NV', 'Nevada'), ('NY', 'New York'), ('WA', 'Washington'), ('CO', 'Colorado')], default='IN', max_length=12)),
                ('platform', models.CharField(choices=[('Facets', 'Facets'), ('CWS', 'CWS')], default='Facets', max_length=12)),
                ('supervisor', models.CharField(default='Preetam Bagi', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]