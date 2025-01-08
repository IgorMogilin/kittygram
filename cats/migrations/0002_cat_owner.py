# Generated by Django 3.2 on 2025-01-08 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='cats.owner'),
            preserve_default=False,
        ),
    ]
